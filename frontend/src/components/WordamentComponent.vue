<template>
  <v-container fluid>
    <h1>Wordament Solver</h1>
    <p>Enter the wordament matrix row by row without spaces</p>
    <v-form class="my-5" @submit.prevent="findWords">
      <v-text-field
          v-model="input"
          :rules="[inputRule]"
          label="Enter 16 letters"
          required
          clearable
      ></v-text-field>
      <v-select label="Word length" v-model="wordLength" :items="[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]"
                required></v-select>
      <v-btn type="submit" color="primary" :disabled="!validInput">Find Words</v-btn>
    </v-form>
    <v-row v-if="searching">
      <v-progress-circular color="blue" indeterminate size="120"/>
    </v-row>
    <v-row v-if="input.length > 0">
      <v-col v-for="(row, index) in matrix" :key="index" cols="12">
        {{ row.join(' ') }}
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <h1>Results</h1>
        <p>Words found: {{ words.length }}</p>
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-row class="mx-3 result-container">
      <v-col v-for="(column, index) in columns" :key="index" cols="3" class="result-column">
        <ul class="result-list">
          <li v-for="(word, i) in sortedWords.slice(column.start, column.end)" :key="i" class="result-list-item">{{ word }}</li>
        </ul>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      input: '',
      wordLength: 3,
      words: [],
      searching: false
    };
  },
  computed: {
    matrix() {
      const matrix = [];
      for (let i = 0; i < 16; i += 4) {
        const row = this.input.slice(i, i + 4).split("").map(str => str.toUpperCase());
        matrix.push(row);
      }
      return matrix;
    },
    columns() {
      let columnWidth = Math.ceil(this.words.length / 4);
      return [
        {start: 0, end: columnWidth},
        {start: columnWidth, end: columnWidth * 2},
        {start: columnWidth * 2, end: columnWidth * 3},
        {start: columnWidth * 3, end: this.words.length}
      ];
    },
    sortedWords() {
      return [...this.words].sort();
    },
    validInput() {
      return /^[a-zA-Z]{16}$/.test(this.input);
    },
    inputRule() {
      return (value) => {
        if (!value) {
          return 'Input is required';
        }
        if (!this.validInput) {
          return 'Input must be exactly 16 letters';
        }
        return true;
      };
    },
  },
  methods: {
    findWords() {
      const matrix = [];
      for (let i = 0; i < 4; i++) {
        const row = [];
        for (let j = 0; j < 4; j++) {
          const index = i * 4 + j;
          row.push(this.input[index].toUpperCase());
        }
        matrix.push(row);
      }
      this.searching = true
      axios.post('http://localhost:5000/api/find-words', {'matrix': matrix, 'n': this.wordLength})
          .then((response) => {
            this.words = response.data.words;
            this.searching = false
          })
          .catch((error) => {
            this.searching = false
            console.log(error);
          });
    },
  },
};
</script>

<style>
.result-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.result-column {
  width: 23%;
  margin-bottom: 32px;
  padding: 16px;
  background-color: #f5f5f5;
  border-radius: 4px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.result-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

.result-list-item {
  margin-bottom: 8px;
  font-size: 16px;
  line-height: 1.2;
  color: #333333;
}

</style>