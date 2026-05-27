// Wait until the entire HTML page is fully loaded in the browser before running code
document.addEventListener("DOMContentLoaded", function () {

  // 1. Log a message to the browser console to verify the file is linked correctly
  console.log("🚀 HallyuHub Core UI Engine Loaded successfully.");

  // 2. Grab references to our HTML elements using their unique IDs or Classes
  const bodyElement = document.body;
  const securityAlarm = document.getElementById("security_alarm");

  // 3. A helper utility function to manually test our "Panic Mode" using JavaScript
  // You can open your browser inspector console and type: triggerJsPanic() to test it!
  window.triggerJsPanic = function () {
    console.warn("⚠️ JavaScript: Manually triggering Panic Mode class override...");

    // Toggle the 'alert-panic' class on the body tag
    bodyElement.classList.add("alert-panic");

    // Print a confirmation message directly inside the security banner
    if (securityAlarm) {
      securityAlarm.innerText = "ATTACK DETECTED BY CLIENT ENGINE // TERMINAL LOCKED";
    }
  };

  // 4. A helper utility function to clear the panic state and return to normal pastel mode
  // You can type: clearJsPanic() in your browser console to reset the site!
  window.clearJsPanic = function () {
    console.log("✨ JavaScript: Resetting UI back to safe pastel mode.");
    bodyElement.classList.remove("alert-panic");

    if (securityAlarm) {
      securityAlarm.innerText = "Intrusion detected.";
    }
  };
});