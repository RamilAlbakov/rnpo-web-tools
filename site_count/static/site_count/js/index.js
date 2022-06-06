const btnIds = ['host-btn', 'vendor-btn', 'region-btn'];

const switchClasses = (divId) => {
    const activeTable = document.getElementsByClassName('active-table')[0];
    activeTable.classList.add('hidden-table');
    activeTable.classList.remove('active-table');

    const element = document.getElementById(divId);
    element.classList.remove('hidden-table');
    element.classList.add('active-table');
}

btnIds.forEach(btnId => {
    divId = btnId.split('-')[0];
    btn = document.getElementById(btnId);
    btn.addEventListener('click', switchClasses.bind(null, divId));
});


const kcellSitesForm = document.getElementById('kcell-sites');
kcellSitesForm.addEventListener('submit', (e) => {
    e.preventDefault();
    submitBtn = document.getElementById('download-excel');
    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span>Loading...';

    const formData = new FormData();
    formData.append('csrfmiddlewaretoken', document.querySelector('[name="csrfmiddlewaretoken"]').value)

    fetch('http://127.0.0.1:8000/site_count/download/', {method: 'POST', body: formData})
    .then(respose => respose.blob())
    .then(data => {
        const url = window.URL.createObjectURL(data);
        const anchor = document.createElement("a");
        anchor.href = url;
        anchor.download = 'site_data.xlsx';
        anchor.click();

        submitBtn.innerHTML = 'Download';
    });
});