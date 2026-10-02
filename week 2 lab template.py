{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lanezzz-zz/CST1510_LABWORK1/blob/main/week%202%20lab%20template.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ll6o-X8x7Vvs"
      },
      "source": [
        "# Week 2 — Lab\n",
        "\n",
        "**3 hours.** Work through in order. You are not expected to finish everything.\n",
        "\n",
        "| Part | Time | What |\n",
        "|---|---|---|\n",
        "| Warm-up | 15 min | Fix three broken programs |\n",
        "| Drills | 60 min | Short tasks on every topic this week, plus two challenges |\n",
        "| Break | 10 min | |\n",
        "| Mini-project | 80 min | Add decisions and a loop to your Record Check |\n",
        "| Wrap-up | 15 min | Cheat sheet notes, photo, push to GitHub |\n",
        "\n",
        "**Aiming for a pass?** Do all the drills in Topics 1–4 and the Threshold version of the mini-project.\n",
        "**Aiming higher?** Add the Typical version of the mini-project.\n",
        "**Aiming for a first?** Add the two Challenge drills and the Excellent version of the mini-project.\n",
        "\n",
        "> ### What you submit this week\n",
        "> Both files stay in this `LAB` folder and are pushed to GitHub at the end of the lab.\n",
        ">\n",
        "> 1. **This notebook**, with your drill answers and the photo of your Cheat Sheet pasted in at the very end\n",
        "> 2. **`template.py`**, your completed mini-project\n",
        ">\n",
        "> The warm-up is not submitted.\n",
        "\n",
        "> ### If you are stuck\n",
        "> 1. Read the **last line** of the error. If there is no error, check what should be stopping your loop.\n",
        "> 2. Check the *Common mistakes* table in that topic's walkthrough.\n",
        "> 3. Run the matching file in that topic's `examples/` folder.\n",
        "> 4. Ask, and say what the last line of the error said."
      ],
      "id": "Ll6o-X8x7Vvs"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-qbicE0z7Vvu"
      },
      "source": [
        "---\n",
        "# Warm-up · 15 min\n",
        "\n",
        "Open the `warmup/` folder. Each file is **broken on purpose**. For each one:\n",
        "\n",
        "1. Run it and read the **last line** of the error first.\n",
        "2. Look at the line number it gives you.\n",
        "3. Fix it and run it again.\n",
        "\n",
        "| Error you will meet | Usually means |\n",
        "|---|---|\n",
        "| `IndentationError` | the line under `if`, `while` or `for` is not indented |\n",
        "| `SyntaxError` | often a missing `:` at the end of an `if`, `while` or `for` line |\n",
        "| `TypeError` | comparing text with a number: did you forget `float()`? |"
      ],
      "id": "-qbicE0z7Vvu"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bnU7kKRt7Vvv"
      },
      "source": [
        "---\n",
        "# Drills\n",
        "\n",
        "The drills follow the four topics from the workshop, in the same order. Each one is short and\n",
        "tests one idea. Run your cell and compare it with the expected output.\n",
        "\n",
        "---\n",
        "## Topic 1 · Comparisons and Boolean logic\n",
        "*Walkthrough: `01 - Comparisons and Boolean Logic`*"
      ],
      "id": "bnU7kKRt7Vvv"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FRAsaCDK7Vvv"
      },
      "source": [
        "### D1. The six comparison operators\n",
        "\n",
        "1. Create `a = 10` and `b = 20`.\n",
        "2. Print the result of each comparison: `a == b`, `a != b`, `a < b`, `a > b`, `a <= b`, `a >= b`\n",
        "\n",
        "**Expected output:** `False`, `True`, `True`, `False`, `True`, `False` (one per line)"
      ],
      "id": "FRAsaCDK7Vvv"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iqrjlVlR7Vvv",
        "outputId": "1f04a04d-5f8d-4b92-e0a1-8f1ee8394a1e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n",
            "True\n",
            "False\n",
            "True\n",
            "False\n"
          ]
        }
      ],
      "source": [
        "# D1\n",
        "a = 10\n",
        "b = 20\n",
        "print(a == b)\n",
        "print(a !=b)\n",
        "print(a < b)\n",
        "print(a > b)\n",
        "print(a <= b)\n",
        "print(a >= b)"
      ],
      "id": "iqrjlVlR7Vvv"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3VqILBQw7Vvw"
      },
      "source": [
        "### D2. `=` stores, `==` asks\n",
        "\n",
        "1. Store the number 50 in a variable called `limit`.\n",
        "2. Print `limit == 50`, then print `limit == 60`.\n",
        "3. Add a comment above each line saying whether it **stores** a value or **asks** a question.\n",
        "\n",
        "**Expected output:** `True`, then `False`"
      ],
      "id": "3VqILBQw7Vvw"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gA0ax6FW7Vvw",
        "outputId": "dd7ad9d0-d30f-474c-a48b-39f5fed5dd75"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True , This stores a value.\n",
            "False ,This asks a quesion.\n"
          ]
        }
      ],
      "source": [
        "# D2\n",
        "limit = 50\n",
        "print(limit == 50, ', This stores a value.')\n",
        "print(limit == 60, ',This asks a quesion.')"
      ],
      "id": "gA0ax6FW7Vvw"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IkRolNtT7Vvx"
      },
      "source": [
        "### D3. A comparison is a value too\n",
        "\n",
        "1. Create `attempts = 4` and `max_attempts = 3`.\n",
        "2. Store the comparison in a variable: `is_locked = attempts >= max_attempts`\n",
        "3. Print `is_locked`, then print `type(is_locked)`.\n",
        "\n",
        "**Expected output:**\n",
        "```\n",
        "True\n",
        "<class 'bool'>\n",
        "```"
      ],
      "id": "IkRolNtT7Vvx"
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "SM0LG2cvArao"
      },
      "id": "SM0LG2cvArao",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C6MGMDMY7Vvx",
        "outputId": "ddfc5f96-7098-481d-9f1c-a347c2b5e738"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True <class 'bool'>\n"
          ]
        }
      ],
      "source": [
        "# D3\n",
        "attempts = 4\n",
        "max_attempts = 3\n",
        "is_locked = attempts >= max_attempts\n",
        "print(is_locked,type(is_locked))"
      ],
      "id": "C6MGMDMY7Vvx"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IoO9vQq87Vvy"
      },
      "source": [
        "### D4. Combining conditions with `and`, `or`, `not`\n",
        "\n",
        "1. Create `percent = 95`.\n",
        "2. Print each of these:\n",
        "   - `percent >= 90 and percent < 100`\n",
        "   - `percent < 50 or percent > 90`\n",
        "   - `not (percent > 90)`\n",
        "\n",
        "**Expected output:** `True`, `True`, `False`\n",
        "\n",
        "Now change `percent` to `40` and run again. Before you run it, predict the three results."
      ],
      "id": "IoO9vQq87Vvy"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dHOZcS9U7Vvy",
        "outputId": "6b843b1c-201b-4d67-f63f-034a67ca3dfc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n",
            "False\n"
          ]
        }
      ],
      "source": [
        "# D4\n",
        "percent = 95\n",
        "print((percent >=90) and (percent < 100))\n",
        "print((percent < 50) or (percent > 90))\n",
        "print(not(percent > 90))\n"
      ],
      "id": "dHOZcS9U7Vvy"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tpUzm_dK7Vvy"
      },
      "source": [
        "---\n",
        "## Topic 2 · `if`, `elif`, `else`\n",
        "*Walkthrough: `02 - if, elif, else`*"
      ],
      "id": "tpUzm_dK7Vvy"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "58jzOUG87Vvy"
      },
      "source": [
        "### D5. `if` on its own\n",
        "\n",
        "1. Create `value = 120` and `limit = 100`.\n",
        "2. Use `if` to print `OVER LIMIT` when `value` is greater than `limit`.\n",
        "\n",
        "**Expected output:** `OVER LIMIT`\n",
        "\n",
        "Now change `value` to `80` and run again. Nothing is printed. Add a comment explaining why."
      ],
      "id": "58jzOUG87Vvy"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LIr_ckqW7Vvz"
      },
      "outputs": [],
      "source": [
        "# D5\n",
        "value = 80\n",
        "limit = 100\n",
        "if value > limit:\n",
        "  print(\"OVERLIMIT\")\n"
      ],
      "id": "LIr_ckqW7Vvz"
    },
    {
      "cell_type": "markdown",
      "source": [
        "Nothing was printed because the value is not greater than the limit so the code stops."
      ],
      "metadata": {
        "id": "sM_oQAsV_wPC"
      },
      "id": "sM_oQAsV_wPC"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jEXCz4OS7Vvz"
      },
      "source": [
        "### D6. `if` / `else`\n",
        "\n",
        "1. Create `value = 87` and `limit = 100`.\n",
        "2. Use `if` / `else`:\n",
        "   - if `value` is greater than `limit`, print `OVER LIMIT`\n",
        "   - otherwise, print `OK`\n",
        "\n",
        "**Expected output:** `OK`\n",
        "\n",
        "Now change `value` to `120` and run again. You should see `OVER LIMIT`."
      ],
      "id": "jEXCz4OS7Vvz"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wtP5Ydlx7Vvz",
        "outputId": "729f894f-cd81-456d-8b02-612ea000aa35"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "OVERLIMIT\n"
          ]
        }
      ],
      "source": [
        "# D6\n",
        "value = 120\n",
        "limit = 100\n",
        "if value > limit:\n",
        "  print('OVERLIMIT')\n",
        "else:\n",
        "  print('OK')"
      ],
      "id": "wtP5Ydlx7Vvz"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e0DLm56h7Vvz"
      },
      "source": [
        "### D7. Three possible results with `if` / `elif` / `else`\n",
        "\n",
        "1. Create `value = 87` and `limit = 100`.\n",
        "2. Calculate the percentage: `percent = (value / limit) * 100`\n",
        "3. Use `if` / `elif` / `else` to print:\n",
        "   - `OVER LIMIT` if `percent` is 100 or more\n",
        "   - `WARNING` if `percent` is 90 or more\n",
        "   - `OK` otherwise\n",
        "\n",
        "**Test it** by changing `value` and running the cell each time:\n",
        "\n",
        "| value | Expected output |\n",
        "|---|---|\n",
        "| 87 | `OK` |\n",
        "| 95 | `WARNING` |\n",
        "| 120 | `OVER LIMIT` |\n",
        "\n",
        "*Hint: check for 100 first. Python runs the first branch that is True and skips the rest.*"
      ],
      "id": "e0DLm56h7Vvz"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SwuuZjYu7Vvz",
        "outputId": "76c9a0fb-3285-4c2e-b01e-9110608255f8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "OK\n"
          ]
        }
      ],
      "source": [
        "# D7\n",
        "value = 87\n",
        "limit = 100\n",
        "percentage = (value/limit)*100\n",
        "if percentage >= 100:\n",
        "  print('OVERLIMIT')\n",
        "elif percentage >= 90:\n",
        "  print('WARNING')\n",
        "else:\n",
        "  print('OK')"
      ],
      "id": "SwuuZjYu7Vvz"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8j0S7-iv7Vvz"
      },
      "source": [
        "### D8. Indentation decides what is inside the `if`\n",
        "\n",
        "The code is already in the cell below.\n",
        "\n",
        "1. **Before you run it**, write a comment predicting what it will print.\n",
        "2. Run it and check your prediction.\n",
        "3. Now indent the last `print` line so it lines up with `print(\"OVER LIMIT\")`. Run it again.\n",
        "4. Add a comment explaining why the output changed.\n",
        "\n",
        "**Expected output:** first `Check finished`, then (after step 3) nothing at all."
      ],
      "id": "8j0S7-iv7Vvz"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J4jgHd1n7Vv0"
      },
      "outputs": [],
      "source": [
        "# D8\n",
        "value = 50\n",
        "limit = 100\n",
        "\n",
        "if value > limit:\n",
        "    print(\"OVER LIMIT\")  #The output will be just check finished because the value is not greater than the limit.\n",
        "    print(\"Check finished\"). #The output has changed because the second print became part of the loop which is already not printing an output because the conditions are not met."
      ],
      "id": "J4jgHd1n7Vv0"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kl8F1JTX7Vv0"
      },
      "source": [
        "---\n",
        "## Topic 3 · `while` loops\n",
        "*Walkthrough: `03 - while Loops`*"
      ],
      "id": "kl8F1JTX7Vv0"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fUqoXDZP7Vv0"
      },
      "source": [
        "### D9. Count from 1 to 10 with `while`\n",
        "\n",
        "1. Create a variable `count = 1`.\n",
        "2. Write a `while` loop that runs while `count` is 10 or less.\n",
        "3. Inside the loop, print `count`, then add 1 to it (`count += 1`).\n",
        "\n",
        "**Expected output:** the numbers 1 to 10, one per line."
      ],
      "id": "fUqoXDZP7Vv0"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pYGn3KJx7Vv0",
        "outputId": "ecc1f7a6-4adc-4045-8325-2047d83abc09"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ],
      "source": [
        "# D9\n",
        "count = 1\n",
        "while count <= 10:\n",
        "  print(count)\n",
        "  count += 1"
      ],
      "id": "pYGn3KJx7Vv0"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BZ9X0QPo7Vv0"
      },
      "source": [
        "### D10. Fix the loop that never stops\n",
        "\n",
        "The code below is broken: it would print `1` forever.\n",
        "\n",
        "1. **Do not run it yet.** Read it and find why the condition never becomes False.\n",
        "2. Fix it, then run it.\n",
        "\n",
        "**Expected output:** the numbers 1 to 5, one per line.\n",
        "\n",
        "*If a loop ever runs forever, click the stop button (■) at the top of the notebook.*"
      ],
      "id": "BZ9X0QPo7Vv0"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xVMe00Mf7Vv0",
        "outputId": "fc30fd98-59f2-455a-f68e-300ce0a31bf4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ],
      "source": [
        "# D10\n",
        "count = 1\n",
        "while count <= 5:\n",
        "    print(count)\n",
        "    break\n"
      ],
      "id": "xVMe00Mf7Vv0"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3o7ZH9ec7Vv0"
      },
      "source": [
        "### D11. `while True` and `break`: add numbers until the user types `done`\n",
        "\n",
        "1. Create a variable `total = 0`.\n",
        "2. Use a `while True:` loop. Inside it, ask: `Enter a number (or done to finish): `\n",
        "3. If the user types `done`, stop the loop with `break`.\n",
        "4. Otherwise, convert what they typed with `float()` and add it to `total`.\n",
        "5. After the loop, print the total.\n",
        "\n",
        "**Example run:**\n",
        "\n",
        "```\n",
        "Enter a number (or done to finish): 5\n",
        "Enter a number (or done to finish): 10\n",
        "Enter a number (or done to finish): 2.5\n",
        "Enter a number (or done to finish): done\n",
        "Total: 17.5\n",
        "```\n",
        "\n",
        "*In a notebook, the input box appears at the top of VS Code. Press Enter after each number.*"
      ],
      "id": "3o7ZH9ec7Vv0"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sgCWdlX27Vv1"
      },
      "outputs": [],
      "source": [
        "# D11\n",
        "total = 0\n",
        "while True:\n",
        "  user_input = input('Enter a number (or done to finish):  ')\n",
        "if user_input == 'done':\n",
        "   break\n",
        "total +=float(user_input)\n",
        "print(f'total : {total}')"
      ],
      "id": "sgCWdlX27Vv1"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9EFj0hXo7Vv1"
      },
      "source": [
        "### D12. `continue`: skip one number\n",
        "\n",
        "Use a `while` loop to print the numbers 1 to 10, but **skip 5** using `continue`.\n",
        "\n",
        "**Expected output:** `1 2 3 4 6 7 8 9 10` (one per line)\n",
        "\n",
        "*Hint: add 1 to your counter **before** the `continue`, or the loop gets stuck on 5.*"
      ],
      "id": "9EFj0hXo7Vv1"
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "ZVLeb4ku7Vv1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "93aedeaa-8e76-45bd-c61f-37a67535e3f5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ],
      "source": [
        "# D12\n",
        "count = 0\n",
        "while count < 10:\n",
        "  count += 1\n",
        "  if count == 5:\n",
        "    continue\n",
        "  print(count)\n"
      ],
      "id": "ZVLeb4ku7Vv1"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5HvLFZjG7Vv1"
      },
      "source": [
        "---\n",
        "## Topic 4 · `for` loops and `range()`\n",
        "*Walkthrough: `04 - for Loops and range`*"
      ],
      "id": "5HvLFZjG7Vv1"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UcvA5H797Vv1"
      },
      "source": [
        "### D13. `range(stop)` and `range(start, stop)`\n",
        "\n",
        "1. Use `for i in range(5):` to print the numbers it gives you.\n",
        "2. Then write a second loop using `range(start, stop)` that prints 1 to 5.\n",
        "\n",
        "**Expected output:** `0 1 2 3 4`, then `1 2 3 4 5` (one per line)\n",
        "\n",
        "*Remember: the `stop` number is never included.*"
      ],
      "id": "UcvA5H797Vv1"
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "WWJbY5707Vv1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "77eca110-7c33-4a5b-de41-24a2aea318c8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n"
          ]
        }
      ],
      "source": [
        "# D13\n",
        "for i in range(5):\n",
        "  print(i)\n",
        "for i in range (1, 6):\n",
        "  print(i)"
      ],
      "id": "WWJbY5707Vv1"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nJdWt__X7Vv1"
      },
      "source": [
        "### D14. `range(start, stop, step)`\n",
        "\n",
        "1. Print every even number from 2 to 20.\n",
        "2. Then write a second loop that counts down from 10 to 1.\n",
        "\n",
        "**Expected output:** `2 4 6 … 20`, then `10 9 8 … 1` (one per line)\n",
        "\n",
        "*Hint: to count down, use a negative step.*"
      ],
      "id": "nJdWt__X7Vv1"
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "ffDdCv2w7Vv2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d99efb67-c51e-4c74-bb12-896f9851a92e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n",
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "# D14\n",
        "for i in range(2, 21, 2):\n",
        "  print(i)\n",
        "for i in range(10, 0, -1):\n",
        "  print(i)"
      ],
      "id": "ffDdCv2w7Vv2"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LQss0ahs7Vv2"
      },
      "source": [
        "### D15. `enumerate()`: the position and the value together\n",
        "\n",
        "1. Create `code = \"A7X\"`.\n",
        "2. Use a `for` loop with `enumerate(code, start=1)` to print each character with its position.\n",
        "\n",
        "**Expected output:**\n",
        "```\n",
        "Character 1: A\n",
        "Character 2: 7\n",
        "Character 3: X\n",
        "```"
      ],
      "id": "LQss0ahs7Vv2"
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "3-opX5P87Vv2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c6c8d086-e4f8-41c0-e539-75a722a14517"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Character 1:  A\n",
            "Character 2:  7\n",
            "Character 3:  X\n"
          ]
        }
      ],
      "source": [
        "# D15\n",
        "for position, character in enumerate('A7X', start = 1):\n",
        "  print(f\"Character {position}:  {character}\")"
      ],
      "id": "3-opX5P87Vv2"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8ITo_IHM7Vv2"
      },
      "source": [
        "### D16. `for` or `while`?\n",
        "\n",
        "Write both programs below. Above each one, add a comment saying which loop you chose and why.\n",
        "\n",
        "a) Ask the user for **exactly 3** numbers, and print each one back.\n",
        "\n",
        "b) Keep asking for a password until the user types `letmein`, then print `Welcome`.\n",
        "\n",
        "*Hint: do you know in advance how many times the loop will run?*"
      ],
      "id": "8ITo_IHM7Vv2"
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "xF8jFlLJ7Vv2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d9fcfa0c-9635-40a0-a534-bc1782746596"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: usecds\n",
            "usecds\n",
            "Enter a number: csibciie\n",
            "csibciie\n",
            "Enter a number: letmein\n",
            "letmein\n",
            "Enter password: letmein\n",
            "Welcome\n"
          ]
        }
      ],
      "source": [
        "# D16\n",
        "for i in range(3):\n",
        "  number = input('Enter a number: ')\n",
        "  print(number)\n",
        "while True:\n",
        "  user_input = input('Enter password: ')\n",
        "  if user_input == 'letmein':\n",
        "    break\n",
        "print('Welcome')"
      ],
      "id": "xF8jFlLJ7Vv2"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vWs6uU4k7Vv2"
      },
      "source": [
        "---\n",
        "## Challenge · for a first\n",
        "\n",
        "*These combine several ideas from this week. There are no step-by-step instructions.*"
      ],
      "id": "vWs6uU4k7Vv2"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hrqazf5L7Vv4"
      },
      "source": [
        "### C1. Check three records in one run\n",
        "\n",
        "Write a `for` loop that runs exactly 3 times. Each time, ask for a `value` and a `limit`,\n",
        "and print `OVER LIMIT` if `value` is greater than `limit`, otherwise `OK`.\n",
        "\n",
        "**Test it** with these three pairs, in this order:\n",
        "\n",
        "| value | limit | Expected output |\n",
        "|---|---|---|\n",
        "| 87 | 100 | `OK` |\n",
        "| 120 | 100 | `OVER LIMIT` |\n",
        "| 45 | 100 | `OK` |"
      ],
      "id": "hrqazf5L7Vv4"
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "AfZycdz77Vv4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8bba2480-d19f-426e-bad8-fa752c700d93"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter value: 87\n",
            "Enter limit: 100\n",
            "OK\n",
            "Enter value: 120\n",
            "Enter limit: 100\n",
            "OVERLIMIT\n",
            "Enter value: 45\n",
            "Enter limit: 100\n",
            "OK\n"
          ]
        }
      ],
      "source": [
        "# C1\n",
        "for i in range(3):\n",
        "  value = int(input('Enter value: '))\n",
        "  limit = int(input('Enter limit: '))\n",
        "\n",
        "\n",
        "  if value > limit:\n",
        "     print('OVERLIMIT')\n",
        "  else:\n",
        "     print('OK')\n"
      ],
      "id": "AfZycdz77Vv4"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X-9RtL4H7Vv4"
      },
      "source": [
        "### C2. Three tries to log in\n",
        "\n",
        "The correct password is `python123`. The user gets **at most 3 tries**.\n",
        "\n",
        "- If they type the correct password, print `Access granted` and stop asking.\n",
        "- If they get it wrong 3 times, print `Account locked`.\n",
        "\n",
        "**Test it twice:**\n",
        "\n",
        "| You type | Expected output |\n",
        "|---|---|\n",
        "| `abc`, then `python123` | `Access granted` (after 2 tries) |\n",
        "| `abc`, `123`, `pass` | `Account locked` |"
      ],
      "id": "X-9RtL4H7Vv4"
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "cJ_lQILy7Vv4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4c9aacf2-9dc7-4e1b-f688-5f7511c2092a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter password : icsbdc\n",
            "Account locked\n",
            "Enter password : sjdncibs\n",
            "Account locked\n",
            "Enter password : python123\n",
            "Access Granted\n"
          ]
        }
      ],
      "source": [
        "# C2\n",
        "coorect_password = 'python123'\n",
        "\n",
        "for i in range(3):\n",
        "  password = input('Enter password : ')\n",
        "\n",
        "  if password == coorect_password:\n",
        "    print('Access Granted')\n",
        "  else:\n",
        "    print('Account locked')"
      ],
      "id": "cJ_lQILy7Vv4"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FTEDEdYI7Vv4"
      },
      "source": [
        "---\n",
        "# Mini-project · 80 min\n",
        "\n",
        "Open **`template.py`** (in this `LAB` folder). It has the structure already — you fill in the marked sections.\n",
        "\n",
        "## Choose your lane\n",
        "\n",
        "Pick **one**. All three are the same program with different words. (You do not have to\n",
        "keep the lane you picked in Week 1.)\n",
        "\n",
        "| Lane | Your three inputs | Example |\n",
        "|---|---|---|\n",
        "| **AI / Data Science** | dataset name, rows loaded, rows expected | `survey_2026`, `1187`, `1200` |\n",
        "| **Cyber Security** | source IP, failed logins, total attempts | `10.0.0.5`, `12`, `400` |\n",
        "| **IT** | hostname, GB used, GB total | `srv-01`, `87`, `120` |\n",
        "\n",
        "## What to build\n",
        "\n",
        "**Threshold — pass standard.** Ask for the three values. Decide `OVER LIMIT` or `OK`\n",
        "using `if` / `else`. Print them back in a bordered report.\n",
        "\n",
        "```\n",
        "==================================\n",
        "  RECORD CHECK  -  srv-01\n",
        "==================================\n",
        "  Used        : 87\n",
        "  Total       : 120\n",
        "  Status      : OK\n",
        "==================================\n",
        "```\n",
        "\n",
        "**Typical.** As above, and it *calculates* two things it was not given — the difference,\n",
        "and the value as a percentage of the total. Use `if` / `elif` / `else` for a 3-tier\n",
        "status: `OVER LIMIT` (100%+), `WARNING` (90%+), otherwise `OK`. All numbers show 2\n",
        "decimal places and are right-aligned so they line up.\n",
        "\n",
        "```\n",
        "==================================\n",
        "  RECORD CHECK  -  srv-01\n",
        "==================================\n",
        "  Used        :      87.00\n",
        "  Total       :     120.00\n",
        "  Free        :      33.00\n",
        "  Percent     :      72.50 %\n",
        "  Status      :         OK\n",
        "==================================\n",
        "```\n",
        "\n",
        "**Excellent.** Wrap the whole thing in a loop so you can check as many records as you\n",
        "like in one run — type `quit` as the label to stop. Keep count of how many records came\n",
        "back `OVER LIMIT` during the session, and print that count once, after the loop ends.\n",
        "\n",
        "## Rules\n",
        "\n",
        "- **Do not type any number you could calculate.**\n",
        "- Convert every value the user gives you to the right type.\n",
        "- **No lists yet**: that is Week 4.\n",
        "\n",
        "## When it works\n",
        "\n",
        "1. Run it three times with different inputs. Does it still look right?\n",
        "2. Run it with a total of `0`. Note the error, but **do not fix it** yet. That comes later."
      ],
      "id": "FTEDEdYI7Vv4"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C43A2RJ27Vv5"
      },
      "source": [
        "---\n",
        "# Optional revision · not submitted\n",
        "\n",
        "If you have time, answer these on paper. They are good revision, but they are not checked.\n",
        "\n",
        "- What does indentation control in Python, and what happens if you get it wrong?\n",
        "- What is the difference between `=` and `==`?\n",
        "- Why can a `while` loop run forever, and what stops that happening by accident?\n",
        "- Which error did you meet most today, and what did it turn out to mean?"
      ],
      "id": "C43A2RJ27Vv5"
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "RECORD CHECK  -  my version\n",
        "===========================\n",
        "\n",
        "Name  : Hala Mohammedalamin\n",
        "Lane  : Cyber\n",
        "Date  : 1st of october 2026\n",
        "\n",
        "Run it:   python template.py\n",
        "\n",
        "Work through the numbered sections in order. Each one tells you what it must do.\n",
        "Delete these instructions as you replace them with your code.\n",
        "\"\"\"\n",
        "\n",
        "# ==================================================================== INPUT\n",
        "# 1. Ask for your three values.\n",
        "#\n",
        "#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed\n",
        "#    - the second is a NUMBER (use float(), not int())\n",
        "#    - the third  is a NUMBER (use float(), not int())\n",
        "\n",
        "label = input('Enter Hostname/IP: ')      # replace with an input() call\n",
        "value = float(input('Enter value: '))     # replace with an input() call, converted with float()\n",
        "limit = float(input('Enter the limit: '))     # replace with an input() call, converted with float()\n",
        "\n",
        "\n",
        "# ================================================================== PROCESS\n",
        "# 2. Work out the difference and the percentage.       [Typical and above]\n",
        "\n",
        "difference =  value - limit   # replace with your calculation\n",
        "percent = (value/limit) * 100      # replace with your calculation\n",
        "# 3. Decide a status and store it in a variable called status.\n",
        "#\n",
        "#    Threshold : if / else        -> \"OVER LIMIT\" or \"OK\"\n",
        "#    Typical   : if / elif / else -> \"OVER LIMIT\" (100% or more),\n",
        "#                                     \"WARNING\" (90% or more), otherwise \"OK\"\n",
        "\n",
        "\n",
        "if percent >= 100:\n",
        "  status = 'OVERLIMIT'\n",
        "elif percent >= 90:\n",
        "  status = 'WARNING'\n",
        "else:\n",
        "  status = 'OK'\n",
        "   # replace with your if / else (or if / elif / else)\n",
        "\n",
        "\n",
        "# =================================================================== OUTPUT\n",
        "# 4. Print the report.\n",
        "#\n",
        "#    Threshold : the three values you were given, plus status, inside a border\n",
        "#    Typical   : add difference and percent, 2 decimal places, right-aligned\n",
        "#    Excellent : wrap sections 1-4 in a loop so you can check as many records\n",
        "#                as you like in one run - type \"quit\" as the label to stop.\n",
        "#                Keep count of how many came back OVER LIMIT and print that\n",
        "#                once, after the loop ends.\n",
        "\n",
        "print()\n",
        "print(\"=\" * 34)\n",
        "print(f\"  RECORD CHECK  -  {label}\")\n",
        "print(\"=\" * 34)\n",
        "\n",
        "print(f'Value:       {value:>10.2f}')\n",
        "print(f'limit:       {limit:>10.2f}')\n",
        "print(f'Difference:  {difference:>10.2f}')\n",
        "print(f'Percentage:  {percent:>10.2f}%')\n",
        "print(f'Status:      {status:>10}')\n",
        "\n",
        "# your report lines go here\n",
        "\n",
        "print(\"=\" * 34)\n",
        "\n",
        "\n",
        "# ==========================================================================\n",
        "# 5. Before you finish:\n",
        "#\n",
        "#    [ ] Run it three times with different numbers\n",
        "#    [ ] Run it with a total of 0 and note the error (do not fix it yet)\n",
        "#    [ ] Check every variable name says what it holds\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Qm2P4UYW2J_",
        "outputId": "7a6d58b9-5d1f-4603-adc7-4270f73f053e"
      },
      "id": "9Qm2P4UYW2J_",
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Hostname/IP: HMHH'\n",
            "Enter value: 67\n",
            "Enter the limit: 100\n",
            "\n",
            "==================================\n",
            "  RECORD CHECK  -  HMHH'\n",
            "==================================\n",
            "Value:            67.00\n",
            "limit:           100.00\n",
            "Difference:      -33.00\n",
            "Percentage:       67.00%\n",
            "Status:              OK\n",
            "==================================\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UGXj55_o7Vv5"
      },
      "source": [
        "---\n",
        "# Wrap-up · 15 min\n",
        "\n",
        "## 1. This week's cheat sheet\n",
        "\n",
        "On the **same sheet of paper** you started in Week 1, add your handwritten notes for this week.\n",
        "This week's cheat sheet should contain notes about:\n",
        "\n",
        "1. **Comparisons:** `==`, `!=`, `<`, `>`, `<=`, `>=`, and why `==` is not the same as `=`\n",
        "2. **Combining conditions:** `and`, `or`, `not`\n",
        "3. **Decisions:** `if` / `elif` / `else` (Python runs the first branch that is True)\n",
        "4. **Indentation:** the indented lines are the ones inside the `if` or the loop\n",
        "5. **`while` loops:** the condition must change; `while True` with `break`; `continue`\n",
        "6. **`for` loops:** `range(stop)`, `range(start, stop, step)` (stop is not included), and `enumerate()`\n",
        "7. **`for` or `while`?** `for` when you know how many times, `while` when you don't\n",
        "\n",
        "Write them in your own words, with a short example for each. Do not copy from the slides."
      ],
      "id": "UGXj55_o7Vv5"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vY4BqVpq7Vv5"
      },
      "source": [
        "---\n",
        "## 2. Add your cheat sheet notes here\n",
        "\n",
        "Take a clear photo of your **whole** cheat sheet page (Week 1 and Week 2 notes), then click into\n",
        "this cell and paste it (`Ctrl+V` / `Cmd+V`), or drag the image file in.\n",
        "\n",
        "*(paste here)*"
      ],
      "id": "vY4BqVpq7Vv5"
    },
    {
      "cell_type": "markdown",
      "source": [
        "![WhatsApp Image 2026-10-02 at 8.20.11 PM.jpeg](data:image/jpeg;base64,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VfcYZcdXWYVefRdfbfUveYeQYUaTZsksqovRVcWESDijuD7n6bQVnkBtrwinVjlqmBibTwdeafZaQQcYekVUYeTVVdaTSXvSQclbXprVkgjjvpU/aVZdxsm8UTcbCmWZWYqrqhu0chggeL0vTSaXRQZUYfcSQcaQTbScddccbrRUQWUaYWaijiiisvrBbph6/c5W8+wrHqoxXPuhcWFPjgVQOx/RaYbYWcVYTUbSTQTYf+gmfpPXTZSRfWisrlfnrvrrPkgYekN29FohrQ3hohr8ZjM8NLIlivRmoYUcRbRWXbYTaYZYRafYXtVUZbZbRdVfUdnnjhkmlvplori2OYgB8vKgPBXrvmj5bR/UFPuouuFYQWUVVTSXWfeZZfSbdaQTUYadrUeflec+UlbingsjnnjmuuyiUNIgmHEExetmmrbTwVrPLTmguJbUQfWUeUeSdUcSbRXaQYQZa9XZQhx7SShqhmikoshjlgrglhhsrimrJGFIxorog0TqCNGMvqhjtFVWULbQVWXVUdVasVcZQQY0tYXctyicQjhapltjrgtluptiJfpjrfoesJjGnhxVNXnhUbCrsujIyMdYYORbbcScbWeWQYeYWUVrbcvplYgosvYrrmspmkrgrlrKIsFLLAoNnDXRVwBHT+WSmkqookqpKVREBaRUTYffZZRUfVcYbcYtvTij/ttjglnhlvijmnnrrstIttCeUHo6jKYXeY8KDMp4xilqkqYZJCGFfVXfdddcTRbfWffeTfwsqXuhlgojrrurpkljhhkstqMlkgmjR64DPVZaajpgInI3RRvqjaEVFIESbfbfddRWXfUWbcZdZtnmZrrshmthlmrrtntpmhotdSGgooieUePlWSYZYOAtuoCVgkljAYWKMFedTUZbbZRacRWVdaacWWZXkvuqvtnnqvsmkqhqhtrvJmmtW2VqUGGVpdQcCHFqYseW+zHiUKNhxQXVfQUVSYaSeTYdSZYvfktupvhmrmottojklivrmsvPnivCwXKgX9Xpqv6OObTdufXXdKXLqt2maXUdZfTTadeYeSdHapdugllmjimonilquqihunlkuGElmiSJh7aEYUfa9d9WFVCVQUbasdvonjlXVTZdXRcQdctQVReXSdtiunhphnnrnqumpsjotumusKpinOKckVdTWa89+zYeOVVeZVdYIkgpsoZT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)"
      ],
      "metadata": {
        "id": "ps5uGp04cHM_"
      },
      "id": "ps5uGp04cHM_"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gs4j6N9S7Vv5"
      },
      "source": [
        "---\n",
        "## 3. Push to GitHub\n",
        "\n",
        "Save this notebook and `template.py`. Then open the `CST1510` folder in VS Code and run these\n",
        "three commands in its terminal:\n",
        "\n",
        "```\n",
        "git add .\n",
        "git commit -m \"Week 2 lab and mini-project\"\n",
        "git push\n",
        "```\n",
        "\n",
        "Finally, open your repository on GitHub and check that this week's `LAB` folder is there.\n",
        "If it is not, type `pwd` in the terminal to check which folder you are in."
      ],
      "id": "gs4j6N9S7Vv5"
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.12"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}