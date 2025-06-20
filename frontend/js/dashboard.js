// Sample mock data
const paymentData = [
  {
    invoice: "INV001",
    vendor: "Vendor A",
    gross: 10000,
    gst: 1800,
    tds: 1000,
    net: 7200,
    date: "2025-06-01"
  },
  {
    invoice: "INV002",
    vendor: "Vendor B",
    gross: 15000,
    gst: 2700,
    tds: 1200,
    net: 11100,
    date: "2025-06-03"
  },
  {
    invoice: "INV003",
    vendor: "Vendor C",
    gross: 20000,
    gst: 3600,
    tds: 2000,
    net: 14400,
    date: "2025-06-05"
  }
];

// Populate the table
const tableBody = document.querySelector("#paymentTable tbody");

paymentData.forEach((payment) => {
  const row = document.createElement("tr");

  row.innerHTML = `
    <td>${payment.invoice}</td>
    <td>${payment.vendor}</td>
    <td>₹${payment.gross}</td>
    <td>₹${payment.gst}</td>
    <td>₹${payment.tds}</td>
    <td>₹${payment.net}</td>
    <td>${payment.date}</td>
  `;

  tableBody.appendChild(row);
});
// Search Filter Logic
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("keyup", () => {
  const filter = searchInput.value.toLowerCase();
  const rows = document.querySelectorAll("#paymentTable tbody tr");

  rows.forEach((row) => {
    const text = row.textContent.toLowerCase();
    row.style.display = text.includes(filter) ? "" : "none";
  });
});

// Export to Excel Logic
function exportTableToExcel(tableID, filename = "Vendor_Payments.xlsx") {
  const table = document.getElementById(tableID);
  const wb = XLSX.utils.table_to_book(table, { sheet: "Payments" });
  XLSX.writeFile(wb, filename);
}
