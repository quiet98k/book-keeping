import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const getMoneyAccounts = () => axios.get(`${API_URL}moneyaccounts/`);
export const getUsers = () => axios.get(`${API_URL}users/`);
export const getTransactions = () => axios.get(`${API_URL}transactions/`);

export const createMoneyAccount = (data) => axios.post(`${API_URL}moneyaccounts/`, data);
export const createUser = (data) => axios.post(`${API_URL}users/`, data);
export const createTransaction = (data) => axios.post(`${API_URL}transactions/`, data);

export const updateMoneyAccount = async (id, data) => {
    try {
        console.log('Sending update request for money account:', id, data);
        const response = await axios.put(`${API_URL}moneyaccounts/${id}/`, data);
        console.log('Update response:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error updating money account:', error.response ? error.response.data : error.message);
        throw error;
    }
};
export const updateUser = async (id, data) => {
    try {
        console.log('Sending update request for user:', id, data);
        const response = await axios.put(`${API_URL}users/${id}/`, data);
        console.log('Update response:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error updating user:', error.response ? error.response.data : error.message);
        throw error;
    }
};
export const updateTransaction = async (id, data) => {
    try {
        console.log('Sending update request for transaction:', id, data);
        const response = await axios.put(`${API_URL}transactions/${id}/`, data);
        console.log('Update response:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error updating transaction:', error.response ? error.response.data : error.message);
        throw error;
    }
};

export const deleteMoneyAccount = (id) => axios.delete(`${API_URL}moneyaccounts/${id}/`);
export const deleteUser = (id) => axios.delete(`${API_URL}users/${id}/`);
export const deleteTransaction = (id) => axios.delete(`${API_URL}transactions/${id}/`);