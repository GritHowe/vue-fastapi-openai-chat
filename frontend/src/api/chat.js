// api/chat.js
import axios from 'axios'

export async function chat(prompt) {
  const res = await axios.post('http://localhost:8000/chat', { prompt });
  return res.data;  // axios 自动解析 JSON
}