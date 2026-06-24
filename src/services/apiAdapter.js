// src/services/apiAdapter.js

// 1. Centralize your configuration
const TRADEXPRESS_BASE_URL = 'https://api.tradexpress.com'; // Replace with actual URL
const AI_BASE_URL = 'https://api.your-ai-provider.com';

export const apiAdapter = {
  // 2. Helper for authenticated requests
  async _request(url, apiKey, options = {}) {
    const headers = {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      ...options.headers
    };
    
    const response = await fetch(url, { ...options, headers });
    
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    return response.json();
  },

  // 3. Trade Data Logic
  async fetchTradeData(endpoint) {
    const apiKey = process.env.TRADEXPRESS_API_KEY;
    if (!apiKey) throw new Error("TRADEXPRESS_API_KEY is missing");
    
    return this._request(`${TRADEXPRESS_BASE_URL}/${endpoint}`, apiKey);
  },

  // 4. AI Suggestion Logic
  async getAISuggestion(prompt) {
    const apiKey = process.env.AI_API_KEY;
    if (!apiKey) throw new Error("AI_API_KEY is missing");

    return this._request(AI_BASE_URL, apiKey, {
      method: 'POST',
      body: JSON.stringify({ prompt })
    });
  }
};
