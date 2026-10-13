function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — Trial 02 · the enquiry form.
   Validates as you type, then says plainly what will happen. There is no server
   in this concept build, so on success it shows exactly what was captured and
   offers the WhatsApp route instead — which is how most of these enquiries will
   actually travel in the real shop.                                            */
(function () {
  "use strict";

  var T = window.WHYNOT_T || fallbackT;

  var form = document.querySelector("[data-contact-form]");
  if (!form) return;

  var statusEl = document.querySelector("[data-form-status]");
  var HELPLINE = "8886222448";
  var EMAIL = "whynot.rayudu@gmail.com";

  var rules = {
    name: function (v) {
      if (!v) return "Please tell us your name.";
      if (v.length < 2) return "That looks a little short.";
      return "";
    },
    mobile: function (v) {
      var digits = v.replace(/[^0-9]/g, "").replace(/^(91)(?=[6-9][0-9]{9}$)/, "");
      if (!v) return "We need a number to call you back on.";
      if (!/^[6-9][0-9]{9}$/.test(digits)) return "Enter the 10-digit mobile number.";
      return "";
    },
    message: function (v) {
      if (!v) return "Tell us what you're looking for.";
      if (v.length < 10) return "A few more words will help us help you.";
      if (v.length > 1200) return "Please keep it under 1200 characters.";
      return "";
    }
  };

  function setError(input, message) {
    var field = input.closest(".field");
    var error = field && field.querySelector(".error");
    var errorId = input.id + "-error";
    var describedBy = input.getAttribute("aria-describedby") || "";

    if (message) {
      input.setAttribute("aria-invalid", "true");
      if (error) error.textContent = message;
      if (describedBy.indexOf(errorId) === -1) {
        input.setAttribute("aria-describedby", (describedBy + " " + errorId).trim());
      }
    } else {
      input.removeAttribute("aria-invalid");
      if (error) error.textContent = "";
    }
    return !message;
  }

  function validate(input) {
    var rule = rules[input.name];
    return rule ? setError(input, rule(input.value.trim())) : true;
  }

  var inputs = ["name", "mobile", "message"]
    .map(function (n) { return form.elements[n]; })
    .filter(Boolean);

  inputs.forEach(function (input) {
    input.addEventListener("blur", function () { validate(input); });
    input.addEventListener("input", function () {
      if (input.getAttribute("aria-invalid") === "true") validate(input);
    });
  });

  /* Pre-fill from a product card: contact.html?about=55-inch%204K%20QLED…
     (this is the "Ask about this" button on every catalogue card) */
  var params = new URLSearchParams(location.search);
  var about = params.get("about");
  if (about && form.elements.message && !form.elements.message.value) {
    form.elements.message.value = "I'd like today's price and availability for: " + about + ".\n\nMy town is ";
  }

  function sendToServer(payload) {
    /* DEMO MODE. In production:
       return fetch("/api/enquiry", { method: "POST", headers: {...},
         body: JSON.stringify(payload) }).then(checkStatus);            */
    return new Promise(function (resolve) { setTimeout(function () { resolve(payload); }, 500); });
  }

  function waLink(payload) {
    return "https://wa.me/91" + HELPLINE + "?text=" + encodeURIComponent(
      "Hi WHYNOT, I'd like today's price.\n\nName: " + payload.name +
      "\nTown: " + (payload.town || "—") +
      "\nMobile: " + payload.mobile +
      "\n\n" + payload.message
    );
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    if (!inputs.map(validate).every(Boolean)) {
      var firstBad = form.querySelector('[aria-invalid="true"]');
      if (firstBad) firstBad.focus();
      if (statusEl) {
        statusEl.innerHTML = "<strong>Almost there.</strong><span>Check the highlighted fields above.</span>";
      }
      return;
    }

    var payload = {
      name: form.elements.name.value.trim(),
      mobile: form.elements.mobile.value.trim(),
      town: (form.elements.town && form.elements.town.value.trim()) || "",
      message: form.elements.message.value.trim()
    };

    var submit = form.querySelector('button[type="submit"]');
    var label = submit ? submit.textContent : "";
    if (submit) { submit.disabled = true; submit.textContent = "Sending…"; }
    if (statusEl) statusEl.innerHTML = "";

    sendToServer(payload)
      .then(function () {
        form.reset();
        inputs.forEach(function (i) { setError(i, ""); });
        if (statusEl) {
          statusEl.innerHTML =
            "<strong>Thanks, " + payload.name.split(" ")[0].replace(/[<>&]/g, "") + ". We have your number.</strong>" +
            "<span>Someone from the showroom nearest to " + (payload.town || "you") +
            " will call " + payload.mobile + " between 10 am and 9 pm — usually much sooner.</span>" +
            '<span><a class="link" href="' + waLink(payload) + '" target="_blank" rel="noopener noreferrer">Send the same message on WhatsApp</a> ' +
            'or call <a class="link" href="tel:+91' + HELPLINE + '">' + HELPLINE + "</a>.</span>" +
            '<span class="card__meta">This is a concept build with no server attached, so nothing has actually been sent. ' +
            'Nothing you typed left this device.</span>';
          statusEl.setAttribute("tabindex", "-1");
          statusEl.focus();
        }
      })
      .catch(function () {
        if (statusEl) {
          statusEl.innerHTML = "<strong>That didn't go through.</strong>" +
            '<span>Please call <a class="link" href="tel:+91' + HELPLINE + '">' + HELPLINE + "</a> instead — it is faster anyway.</span>";
        }
      })
      .then(function () {
        if (submit) { submit.disabled = false; submit.textContent = label; }
      });
  });

  /* redraw the generated markup when the language changes */
  window.WHYNOT_RERENDER = function () { var s = document.querySelector('[data-form-status]'); if (s && s.textContent) { s.textContent = s.textContent; } };

})();
