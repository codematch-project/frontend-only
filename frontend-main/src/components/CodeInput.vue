<template>
  <div class="code-input">
    <h1>Code Similarity Detection</h1>
    <textarea 
      v-model="code" 
      placeholder="Enter code ..." 
      :maxlength="maxChars"
    ></textarea>
    <p>{{ remainingChars }} characters remaining</p>
    <button @click="submitCode">Submit</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      code: this.$route.query.code || "",
      maxChars: 2000
    };
  },
  computed: {
    remainingChars() {
      return this.maxChars - this.code.length;
    }
  },
  watch: {
    "$route.query.code"(newCode) {
      if (newCode) {
        this.code = newCode;
      }
    }
  },
  methods: {
    async submitCode() {
      if (this.code.length > this.maxChars) {
        alert("Code input exceeds the 2000 character limit.");
        return;
      }
      try {
        // Send the code to the FastAPI backend
        const response = await axios.post("http://localhost:8000/process_code", { code: this.code });
        const results = response.data; // Get the results from the response
        console.log("Received results from backend:", results); // Log the response data


        // Navigate to the Results page and pass the code and results as query parameters
        this.$router.push({ 
          path: "/results", 
          query: { code: this.code, results: JSON.stringify(results) }
        });
      } catch (error) {
        console.error("Error sending code to backend:", error);
        alert("Failed to send the code to the backend. Check the console for details.");
      }
    }
  }
};
</script>

<style scoped>
.code-input {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
textarea {
  width: 50%;
  height: 200px;
  margin-bottom: 10px;
  padding: 10px;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #000;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #333;
}
</style>
