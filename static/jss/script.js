document.addEventListener("DOMContentLoaded", function () {
  const bodyElement = document.body;
  const securityAlarm = document.getElementById("security_alarm");

  window.triggerJsPanic = function () {
    bodyElement.classList.add("alert-panic");
    if (securityAlarm) {
      securityAlarm.innerText = "ATTACK DETECTED BY CLIENT ENGINE // TERMINAL LOCKED";
    }
  };

  window.clearJsPanic = function () {
    bodyElement.classList.remove("alert-panic");
    if (securityAlarm) {
      securityAlarm.innerText = "Intrusion detected.";
    }
  };

  const navLinks = document.querySelectorAll("header nav ul li a");
  const currentWindowPath = window.location.pathname;

  navLinks.forEach(function (link) {
    if (link.getAttribute("href") === currentWindowPath) {
      link.classList.add("active");
    }
  });

  const navbarMenu = document.querySelector("header nav");
  if (navbarMenu) {
    navbarMenu.addEventListener("click", function (event) {
      if (bodyElement.classList.contains("alert-panic")) {
        event.preventDefault();
        if (securityAlarm) {
          securityAlarm.style.transform = "scale(1.05)";
          setTimeout(() => {
            securityAlarm.style.transform = "scale(1)";
          }, 100);
        }
      }
    });
  }
});