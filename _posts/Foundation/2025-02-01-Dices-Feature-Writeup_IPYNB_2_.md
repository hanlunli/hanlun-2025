---
layout: post
title: Dices Writeup
permalink: /Dices_Writeup
comments: True
categories: blog
---

# Backend

### Dice Class:
- uses random number generator for betting logic (Random package in java)
- calculates winnings based off of betSize and winChance
- Returns a negative amount for losses and a scaled reward for wins.

### Dice Api Controller
- Receives bet requests from the frontend via POST /api/casino/dice/calculate.
- Retrieves user details from the PersonJpaRepository using a unique UID.
- Validates balance before processing a bet.
- Updates and saves the new balance in the database.

# Frontend

### UI
- slider for winChance, input box for bet size (min 1000)
- graph to display winnings over time (will be integrated into bank)
- error handling for bet errors/login issues

![Mermaid Diagram](../../../hanlun-2025/assets/mermaid/20d003583b806d52f74620aa7fb7284081057629f8c553fccfd28a923803358f.png)

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({startOnLoad:true});
</script>
