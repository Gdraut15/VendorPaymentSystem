document.addEventListener("DOMContentLoaded", () => {
    const amount = document.getElementById("amount");
    const gst = document.getElementById("gst");
    const tds = document.getElementById("tds");
  
    const resultBox = document.createElement("div");
    resultBox.id = "autoCalculation";
    document.getElementById("paymentForm").appendChild(resultBox);
  
    function updateNetAmount() {
      const gross = parseFloat(amount.value) || 0;
      const gstAmt = gross * (parseFloat(gst.value) || 0) / 100;
      const tdsAmt = gross * (parseFloat(tds.value) || 0) / 100;
      const net = gross - gstAmt - tdsAmt;
  
      resultBox.innerHTML = `
        <hr>
        <strong>GST Deduction:</strong> ₹${gstAmt.toFixed(2)}<br>
        <strong>TDS Deduction:</strong> ₹${tdsAmt.toFixed(2)}<br>
        <strong>Net Amount Payable:</strong> ₹${net.toFixed(2)}
      `;
    }
  
    [amount, gst, tds].forEach(input => input.addEventListener("input", updateNetAmount));
  });
  