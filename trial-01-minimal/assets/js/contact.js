function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — contact form.
   Validation happens on the client so nobody types a whole message and only
   then learns the mobile number was wrong. There is no server here: this file
   runs in "demo" mode and says so on screen (see index of strings below).
   Swapping in a real endpoint = replace sendToServer().                    */
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

  function fieldEl(input) { return input.closest(".field"); }

  function setError(input, message) {
    var field = fieldEl(input);
    var error = field && field.querySelector(".error");
    var describedBy = input.getAttribute("aria-describedby") || "";
    var errorId = input.id + "-error";

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
    /* Blur is the polite moment to complain; typing is not. */
    input.addEventListener("blur", function () { validate(input); });
    input.addEventListener("input", function () {
      if (input.getAttribute("aria-invalid") === "true") validate(input);
    });
  });

  function sendToServer(payload) {
    /* DEMO MODE — no backend in this trial.
       Production: POST to your CRM / WhatsApp Business API / email relay:
         return fetch("/api/enquiry", {
           method: "POST",
           headers: { "Content-Type": "application/json" },
           body: JSON.stringify(payload)
         }).then(function (r) {
           if (!r.ok) throw new Error("Request failed");
           return r.json();
         });                                                   */
    return new Promise(function (resolve) { setTimeout(function () { resolve(payload); }, 550); });
  }

  function summary(payload) {
    var subject = encodeURIComponent("Website enquiry — " + payload.name);
    var body = encodeURIComponent(
      "Name: " + payload.name + "\nMobile: " + payload.mobile + "\nProduct interest: " + payload.interest +
      "\nTown: " + (payload.town || "—") + "\n\n" + payload.message
    );
    return "mailto:" + EMAIL + "?subject=" + subject + "&body=" + body;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var ok = inputs.map(validate).every(Boolean);
    if (!ok) {
      var firstBad = form.querySelector('[aria-invalid="true"]');
      if (firstBad) firstBad.focus();
      if (statusEl) {
        statusEl.innerHTML = "<strong>Almost there.</strong><span>Please check the highlighted fields above.</span>";
      }
      return;
    }

    var payload = {
      name: form.elements.name.value.trim(),
      mobile: form.elements.mobile.value.trim(),
      interest: (form.querySelector('input[name="interest"]:checked') || {}).value || "Not specified",
      town: (form.elements.town && form.elements.town.value.trim()) || "",
      message: form.elements.message.value.trim()
    };

    var submit = form.querySelector('button[type="submit"]');
    var original = submit ? submit.textContent : "";
    if (submit) { submit.disabled = true; submit.textContent = "Sending…"; }
    if (statusEl) statusEl.innerHTML = "";

    sendToServer(payload)
      .then(function () {
        form.reset();
        inputs.forEach(function (i) { setError(i, ""); });
        if (statusEl) {
          statusEl.innerHTML =
            "<strong>Thanks, " + payload.name.split(" ")[0].replace(/[<>&]/g, "") + ". We'll call you on " +
            payload.mobile + ".</strong>" +
            "<span>Nothing left to do — a person from the showroom will ring you between 10 am and 9 pm. " +
            'In a hurry? Call <a class="link" href="tel:+91' + HELPLINE + '">' + HELPLINE + "</a>.</span>" +
            '<span class="form__note">Demo build: this trial has no server attached, so nothing was actually sent. ' +
            'Send it by email instead: <a class="link" href="' + summary(payload) + '">open in your mail app</a>.</span>';
          statusEl.setAttribute("tabindex", "-1");
          statusEl.focus();
        }
      })
      .catch(function () {
        if (statusEl) {
          statusEl.innerHTML = "<strong>That didn't go through.</strong>" +
            '<span>Please call <a class="link" href="tel:+91' + HELPLINE + '">' + HELPLINE + "</a> instead — it's faster anyway.</span>";
        }
      })
      .then(function () {
        if (submit) { submit.disabled = false; submit.textContent = original; }
      });
  });

  /* redraw the generated markup when the language changes */
  window.WHYNOT_RERENDER = function () { var s = document.querySelector('[data-form-status]'); if (s && s.textContent) { s.textContent = s.textContent; } };

})();
