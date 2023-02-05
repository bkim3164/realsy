import { React, useState } from 'react'
import '../App.css'
import Form from 'react-bootstrap/Form';
import logo from '../realsy_logo.png'
import { Navigate, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Card from './Card.js'



function SearchPage() {
    const [location, setLocation] = useState('');
    const [result, setResult] = useState('');
    const navigate = useNavigate();
    const handleSubmit = event => {
        console.log(location)
        event.preventDefault();
        const updateDate = async () => {
            const API_ENDPOINT = "http://localhost:8000/get-location";
            const res = await axios.post(API_ENDPOINT, { location: location });
            //console.log(res.data)
            setResult(res.data)


        }
        updateDate()



    };
    if (result) {
        return (
            <div className="CardPage">
                <Card {...result} />
            </div>
        );
    }
    return (
        <div className="SearchPage">
            <img id="logo2" src={logo} alt="Realsy logo"></img>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="formLocation">
                    <h1>Hello, fellow client!</h1>
                    <h1>What is your desired location?</h1>
                    <label id="form-submission"> Location: <input onChange={event => setLocation(event.target.value)} type="string" id="location" value={location} placeholder="City, State (If city has more than one word, uses dashes!) " /></label>
                </Form.Group>
                <input type="submit" id="submit" placeholder="Submit" name="submit" />
            </Form>
        </div>
    );
}


export default SearchPage