<template>
  <div class="results">
    <h2>Code Similarity Detection Results</h2>
    <div class="content">
      <!-- Left Column: Code Display and Refresh Button -->
      <div class="code-display">
        <textarea 
          v-model="code" 
          readonly 
          placeholder="The code you entered will appear here..."
        ></textarea>
        <button @click="refreshResults">Refresh</button>
      </div>
      
      <!-- Right Column: 10 Results -->
      <div class="result-list">
        <h3>10 Results</h3>
        <ul>
          <li v-for="(result, index) in results" :key="index">
            <a :href="result.link" target="_blank">
              <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="20" />
              {{ result.link }}
            </a>
            <!-- Accessing stars and similarity from metadata -->
            <span>{{ result.metadata.language }} | {{ result.metadata.stars }} stars | {{ result.metadata.similarity }} similarity</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      code: this.$route.query.code || "", // Retrieve the code from the query parameter
      results: JSON.parse(this.$route.query.results || "[]") // Parse the results from the query parameter
    };
  },
  methods: {
    refreshResults() {
      // Redirect to the Code Input page with the existing code in the query parameter
      this.$router.push({ path: "/", query: { code: this.code } });
    }
  },
  mounted() {
    if (!this.results.length) {
      console.warn("No results received from backend.");
    }
  }
  
};
</script>

<style scoped>
.results {
  padding: 20px;
  text-align: center;
}
.content {
  display: flex;
  justify-content: space-between; /* Distribute space evenly between left and right columns */
  align-items: flex-start; /* Align items to the top */
}
.code-display {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Align items to the left */
  width: 40%; /* Width of the left column */
}
textarea {
  width: 100%;
  height: 200px;
  margin-bottom: 10px;
  padding: 10px;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: none;
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
.result-list {
  width: 55%; /* Width of the right column */
  text-align: left; /* Align text to the left in the result list */
}
ul {
  list-style: none;
  padding: 0;
}
li {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}
a {
  margin-right: 10px;
}
</style>
