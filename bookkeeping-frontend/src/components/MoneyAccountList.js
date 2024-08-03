import React, { useState, useEffect } from 'react';
import { getMoneyAccounts, createMoneyAccount, updateMoneyAccount, deleteMoneyAccount } from '../services/apiService';

const MoneyAccountList = () => {
    const [moneyAccounts, setMoneyAccounts] = useState([]);
    const [newAccount, setNewAccount] = useState({ name: '', balance: '', currency: '' });
    const [updatedBalances, setUpdatedBalances] = useState({});

    useEffect(() => {
        fetchMoneyAccounts();
    }, []);

    const fetchMoneyAccounts = async () => {
        const response = await getMoneyAccounts();
        setMoneyAccounts(response.data);
    };

    const handleCreate = async () => {
        await createMoneyAccount(newAccount);
        fetchMoneyAccounts();
    };

    const handleUpdate = async (id, updatedAccount) => {
        console.log('Updating account with ID:', id);
        console.log('Updated account data:', updatedAccount);
        try {
            await updateMoneyAccount(id, updatedAccount);
            fetchMoneyAccounts();
        } catch (error) {
            console.error('Error updating account:', error);
        }
    };

    const handleDelete = async (id) => {
        await deleteMoneyAccount(id);
        fetchMoneyAccounts();
    };

    const handleBalanceChange = (id, newBalance) => {
        setUpdatedBalances({ ...updatedBalances, [id]: newBalance });
    };

    return (
        <div>
            <h1>Money Accounts</h1>
            <input
                type="text"
                placeholder="Name"
                value={newAccount.name}
                onChange={(e) => setNewAccount({ ...newAccount, name: e.target.value })}
            />
            <input
                type="text"
                placeholder="Balance"
                value={newAccount.balance}
                onChange={(e) => setNewAccount({ ...newAccount, balance: e.target.value })}
            />
            <input
                type="text"
                placeholder="Currency"
                value={newAccount.currency}
                onChange={(e) => setNewAccount({ ...newAccount, currency: e.target.value })}
            />
            <button onClick={handleCreate}>Create</button>
            <ul>
                {moneyAccounts.map((account) => (
                    <li key={account.id}>
                        {account.name} - {account.balance} {account.currency}
                        <input
                            type="text"
                            placeholder="New Balance"
                            value={updatedBalances[account.id] || ''}
                            onChange={(e) => handleBalanceChange(account.id, e.target.value)}
                        />
                        <button onClick={() => handleUpdate(account.id, { ...account, balance: updatedBalances[account.id] })}>Update</button>
                        <button onClick={() => handleDelete(account.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MoneyAccountList;