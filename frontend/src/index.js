import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Home extends React.Component {
    render() {
        return (
            <div className="c-align">
                <h1>Library Management</h1>
            </div>
        )
    }
}

ReactDOM.render(<Home />, document.getElementById('root'));