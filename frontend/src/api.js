import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000";


const api = axios.create({
    baseURL: API_BASE_URL,
    headers : {
        'Content-Type': 'application/json',
    }
})

export const getCards = async () => {
    try {
        const response = await api.get(`${API_BASE_URL}/api/v1/cards/`);
        return response.data;
    }
    catch (error) {
        console.error("error: ", error);
        return null;
    }
}



export default api;