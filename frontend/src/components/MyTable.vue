<template>
  <v-row justify="center">
    <v-card>
      <v-card-title>Input Matrix</v-card-title>
      <v-card-text>
        <v-table hide-default-footer>
          <tbody>
          <tr v-for="(row, i) in data" :key="i">
            <td v-for="(char, j) in row" :key="j">{{ char }}</td>
          </tr>
          </tbody>
        </v-table>
      </v-card-text>
    </v-card>
  </v-row>
</template>

<script>
export default {
  props: {
    data: {
      type: Array,
      required: true
    }
  },
  computed: {
    headers() {
      return Array.from({length: 4}, (_, index) => ({
        text: `Column ${index + 1}`,
        value: `column_${index + 1}`
      }))
    },
    items() {
      return this.data.map((row, index) => ({
        ...row.reduce((acc, letter, index) => {
          acc[`column_${index + 1}`] = letter
          return acc
        }, {}),
        id: index
      }))
    }
  }
}
</script>
