// src/services/userAPIService.js

import axios from "axios";
import { API_BASE_URL, API_VERSION } from "@/config";

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const registration = (data) => {
  return apiClient.post(`/api/${API_VERSION}/registration`, data);
};
