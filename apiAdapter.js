// src/apiAdapter.js

export const fetchData = async (tableName) => {
  try {
    // Assuming your Python service is exposed via an API endpoint
    const response = await fetch(`/api/data/${tableName}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error("Failed to fetch data:", error);
    return [];
  }
};
