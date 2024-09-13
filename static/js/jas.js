//Order ongoing
const orders = [
    { id: 1, name: 'Order #001' },
    { id: 2, name: 'Order #002' },
    { id: 3, name: 'Order #003' }
];

// Populate the dropdown with orders
const orderSelect = document.getElementById('orderSelect');
orders.forEach(order => {
    const option = document.createElement('option');
    option.value = order.id;
    option.textContent = order.name;
    orderSelect.appendChild(option);
});

// Handle form submission
document.getElementById('orderForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    const selectedOrderId = document.getElementById('orderSelect').value;
    const selectedOrder = orders.find(order => order.id == selectedOrderId);
    const orderDisplay = document.getElementById('orderDisplay');
    
    if (selectedOrder) {
        orderDisplay.innerHTML = `<p>Selected Order: ${selectedOrder.name}</p>`;
    } else {
        orderDisplay.innerHTML = '<p>Please select a valid order from the dropdown.</p>';
    }
});

//Order Entry Form
function cancelOrder() {
    // Implement cancel action here, e.g., clear the form or redirect
    document.getElementById('orderEntryForm').reset();
}


