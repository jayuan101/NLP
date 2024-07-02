{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOX1n6kQLgLBfcJL2/1NjFS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jayuan101/NLP/blob/main/app_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "lHRo0RU_QYtE"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from transformers import pipeline"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Load the dataset\n",
        "data_path = 'spam.csv'\n",
        "df = pd.read_csv(data_path, encoding='latin-1') # Try 'latin-1' encoding"
      ],
      "metadata": {
        "id": "OBvAmLU0QahP"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Streamlit app\n",
        "st.title(\"Healthcare Data and NLP App\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4XNMN8AXQal_",
        "outputId": "ba355a14-057d-4c12-e092-1c851319dc1a"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-07-02 02:52:31.303 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Display the dataset\n",
        "st.header(\"Healthcare Dataset\")\n",
        "st.dataframe(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vCPwho58Qaow",
        "outputId": "2491cce8-fc5b-4b7c-cbc8-b96afc0f2e4f"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# User input for NLP\n",
        "st.header(\"NLP Text Generation\")\n",
        "user_input = st.text_input(\"Enter a prompt for text generation:\")\n",
        "max_length = st.slider(\"Max length of generated text\", 50, 300, 100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6ZtltCvOQaq_",
        "outputId": "7efbba99-34bb-4e69-b01e-c4375e2f70f4"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-07-02 02:52:31.359 Session state does not function when running a script without `streamlit run`\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if user_input:\n",
        "    generated_text = text_generator(user_input, max_length=max_length, num_return_sequences=1)[0]['generated_text']\n",
        "    st.subheader(\"Generated Text\")\n",
        "    st.write(generated_text)"
      ],
      "metadata": {
        "id": "cqAT9jPrQat3"
      },
      "execution_count": 6,
      "outputs": []
    }
  ]
}
