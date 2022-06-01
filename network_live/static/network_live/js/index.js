const nlForm = document.getElementById('network_live');

nlForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const submitBtn = document.getElementById('nl-submit');
    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span>Loading...';

    const formData = new FormData();
    checkboxes = document.querySelectorAll('.form-check-input:checked');
    checkboxes.forEach(checkbox => {
        formData.append('technologies[]', checkbox.value);
    });
    formData.append('csrfmiddlewaretoken', document.querySelector('[name="csrfmiddlewaretoken"]').value)

    fetch('http://127.0.0.1:8000/network_live/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(data => {
        const url = window.URL.createObjectURL(data);
        const anchor = document.createElement("a");
        anchor.href = url;
        anchor.download = 'kcell_cells.xlsx';
        anchor.click();

        submitBtn.innerHTML = 'Download';
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        })
    });
});
