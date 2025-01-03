const axios = require('axios');

const client_id = '1898519';
const api_key = '7441b4a6-0424-48a3-bb95-f28a20e678a2';

const url = "https://api-seller.ozon.ru/v1/warehouse/list";

const headers = {
    'Api-Key': api_key,
    'Client-Id': client_id
};

axios.post(url, {}, { headers: headers })
    .then(response => {
        console.log(1234);
        const data = response.data;
        console.log(data);
    })
    .catch(error => {
        console.error(error);
    });

// document.write('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS');
