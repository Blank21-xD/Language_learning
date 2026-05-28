document.addEventListener("DOMContentLoaded", function () {

  console.log("🚀 HallyuHub Core UI Engine Loaded successfully.");

  const bodyElement = document.body;
  const securityAlarm = document.getElementById("security_alarm");

  // Interactive manual check utilities for console analysis
  window.triggerJsPanic = function () {
    console.warn("⚠️ JavaScript: Manually triggering Panic Mode class override...");
    bodyElement.classList.add("alert-panic");

    if (securityAlarm) {
      securityAlarm.innerText = "ATTACK DETECTED BY CLIENT ENGINE // TERMINAL LOCKED";
    }
  };

  window.clearJsPanic = function () {
    console.log("✨ JavaScript: Resetting UI back to safe pastel mode.");
    bodyElement.classList.remove("alert-panic");

    if (securityAlarm) {
      securityAlarm.innerText = "Intrusion detected.";
    }
  };

  // Automatic Navigation Active State Link Detection
  const navLinks = document.querySelectorAll("header nav ul li a");
  const currentWindowPath = window.location.pathname;

  navLinks.forEach(function (link) {
    if (link.getAttribute("href") === currentWindowPath) {
      link.classList.add("active");
    }
  });
});