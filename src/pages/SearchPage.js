import { React, useState } from 'react'
import '../App.css'
import Form from 'react-bootstrap/Form';
import logo from '../realsy_logo.png'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';



function SearchPage() {
    const [location, setLocation] = useState('');
    const navigate = useNavigate();

    const handleSubmit = event => {
        console.log(location)
        event.preventDefault();
        const updateDate = async () => {
            const API_ENDPOINT = "http://localhost:8000/get-location";
            const res = await axios.post(API_ENDPOINT, { location: location });
            console.log(res.data)
            setLocation('')


        }
        updateDate()

        

    };
    return (
        <div className="SearchPage">
            <img id="logo2" src={logo} alt="Realsy logo"></img>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="formLocation">
                    <h1>Hello, fellow client!</h1>
                    <h1>What is your desired location?</h1>
                    <label id="form-submission"> Location: <input onChange={event => setLocation(event.target.value)} type="string" id="location" value={location} placeholder="City, State" /></label>
                </Form.Group>
                <input type="submit" id="submit" placeholder="Submit" name="submit" />
            </Form>
        </div>
    );
}


export default SearchPage