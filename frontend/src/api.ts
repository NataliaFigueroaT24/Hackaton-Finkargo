import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const createSupportCase = async (caseData: any) => {
  const response = await axios.post(`${API_URL}/support_cases/`, caseData);
  return response.data;
};

export const getSupportCase = async (caseId: number) => {
  const response = await axios.get(`${API_URL}/support_cases/${caseId}`);
  return response.data;
};
