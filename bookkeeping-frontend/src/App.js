import React from 'react';
import './App.css';
import MoneyAccountList from './components/MoneyAccountList';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>My Money Accounts</h1>
                <MoneyAccountList />
            </header>
        </div>
    );
}

export default App;