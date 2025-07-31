/**
 * Base JavaScript functionality for the Django Online Marketplace
 * Handles logout modal interactions and user authentication flow
 */

/**
 * Shows the logout confirmation modal
 */
function showLogoutModal() {
  document.getElementById("logoutModal").classList.remove("hidden");
}

/**
 * Hides the logout confirmation modal
 */
function hideLogoutModal() {
  document.getElementById("logoutModal").classList.add("hidden");
}

/**
 * Initialize logout functionality when DOM is loaded
 */
document.addEventListener("DOMContentLoaded", function () {
  // Handle logout confirmation
  const confirmLogoutBtn = document.getElementById("confirmLogout");
  if (confirmLogoutBtn) {
    confirmLogoutBtn.addEventListener("click", function () {
      // Create a form to handle the POST request for logout
      const form = document.createElement("form");
      form.method = "POST";
      form.action = window.logoutUrl; // Use the logout URL from global variable

      // Add CSRF token from global variable
      const csrfInput = document.createElement("input");
      csrfInput.type = "hidden";
      csrfInput.name = "csrfmiddlewaretoken";
      csrfInput.value = window.csrfToken;
      form.appendChild(csrfInput);

      document.body.appendChild(form);
      form.submit();
    });
  }

  // Close modal when clicking outside of it
  const logoutModal = document.getElementById("logoutModal");
  if (logoutModal) {
    logoutModal.addEventListener("click", function (event) {
      if (event.target === this) {
        hideLogoutModal();
      }
    });
  }

  // Close modal with Escape key
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      const modal = document.getElementById("logoutModal");
      if (modal && !modal.classList.contains("hidden")) {
        hideLogoutModal();
      }
    }
  });
});
