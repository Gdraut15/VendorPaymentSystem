document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('vendorForm');
  
    form.addEventListener('submit', function (e) {
      const name = form.name.value.trim();
      const company = form.company.value.trim();
      const email = form.email.value.trim();
      const mobile = form.mobile.value.trim();
  
      let isValid = true;
      let errorMessage = "";
  
      // Name validation
      if (name === "") {
        errorMessage += "Name is required.\n";
        isValid = false;
      }
  
      // Company validation
      if (company === "") {
        errorMessage += "Company name is required.\n";
        isValid = false;
      }
  
      // Email format validation
      const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
      if (!emailPattern.test(email)) {
        errorMessage += "Enter a valid email address.\n";
        isValid = false;
      }
  
      // Mobile number validation
      const mobilePattern = /^[0-9]{10}$/;
      if (!mobilePattern.test(mobile)) {
        errorMessage += "Enter a valid 10-digit mobile number.\n";
        isValid = false;
      }
  
      // Prevent form submission if invalid
      if (!isValid) {
        e.preventDefault();
        alert(errorMessage);
      }
    });
  });
  