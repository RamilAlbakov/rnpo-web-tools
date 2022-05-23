const btnIds = ['host-btn', 'vendor-btn', 'region-btn'];

const switchClasses = (divId) => {
    console.log(divId);
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


const download = document.getElementById('download_excel')
download.addEventListener('click', () => {
    download.innerHTML = '<span class="spinner-border spinner-border-sm"></span>Loading...';
    fetch('http://127.0.0.1:8000/site_count/download/')
        .then(response => {
            console.log(response.ok);
            download.innerHTML = "Download";
        });
});