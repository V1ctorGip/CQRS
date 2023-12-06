document.getElementById('createForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    createItem(name, description);
});

document.getElementById('updateForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const id = document.getElementById('updateId').value;
    const name = document.getElementById('updateName').value;
    const description = document.getElementById('updateDescription').value;
    updateItem(id, name, description);
});

function createItem(name, description) {
    fetch('/items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, description })
    }).then(() => fetchItems());
}

function updateItem(id, name, description) {
    fetch(`/items/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, description })
    }).then(() => fetchItems());
}

document.getElementById('deleteForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const id = document.getElementById('deleteId').value;
    deleteItem(id);
});

function deleteItem(id) {
    fetch(`/items/${id}`, {
        method: 'DELETE'
    }).then(() => fetchItems());  // Atualiza a lista após a exclusão
}

function fetchItems() {
    fetch('http://localhost:5001/items') // URL atualizada para apontar para o serviço de consultas
        .then(response => response.json())
        .then(items => {
            const itemsList = document.getElementById('itemsList');
            itemsList.innerHTML = '';
            items.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = `ID: ${item.id}, Name: ${item.name}, Description: ${item.description}`;
                itemsList.appendChild(listItem);
            });
        }).catch(error => console.error('Error fetching items:', error));
}

// Chamar fetchItems ao carregar a página para mostrar a lista atualizada de itens
fetchItems();
