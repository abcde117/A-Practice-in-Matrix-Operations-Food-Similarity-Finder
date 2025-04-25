# 🧮 Food Similarity Finder  
*A Practice in Matrix Operations*

## 📌 Overview / 概要

This project explores matrix operations by comparing the nutritional vectors of different food items. It uses **cosine similarity** and **Euclidean distance** to find which foods are most similar to each other in terms of nutritional composition.

このプロジェクトは、異なる食品の栄養ベクトルを比較することで、行列演算の理解を深めることを目的としています。**コサイン類似度**や**ユークリッド距離**を用いて、栄養成分が類似している食品を特定します。

---

## 🧠 Features / 機能

- Calculates similarity between foods based on their nutritional data  
- Uses **cosine similarity** and **Euclidean distance**  
- Returns ranked list of most similar foods  
- Handles custom datasets in CSV format  

- 栄養データに基づいた食品の類似性を計算  
- **コサイン類似度**と**ユークリッド距離**の2種類を実装  
- 最も類似する食品をランキング形式で出力  
- CSV形式のデータに対応

---

## 🗂️ Files / ファイル構成

- `food_sim_finder.ipynb`: Main notebook with food similarity functions
- `24.csv`: Nutritional data for different food items
- `food_han_new.csv`: Another dataset for nutritional data  

Please upload `24.csv` and `food_han_new.csv` files before running the notebook. You can download example files or use your own custom food data in CSV format.

- `food_sim_finder.ipynb`: 主な食品類似性計算のためのノートブック
- `24.csv`: 異なる食品の栄養データ
- `food_han_new.csv`: もう一つの栄養データセット

ノートブックを実行する前に `24.csv` と `food_han_new.csv` ファイルをアップロードしてください。サンプルファイルをダウンロードするか、独自の食品データをCSV形式で使用できます。

---

## 📊 Methods / 使用した手法

- `cos_similarity(x, y)`: Computes cosine similarity between two vectors  
- `distance.euclidean(x, y)`: Computes Euclidean distance  
- Vector data is normalized and reshaped using NumPy

- コサイン類似度関数とユークリッド距離を活用  
- NumPyを用いたベクトルの整形と演算処理

---

## 📎 Requirements / 必要なライブラリ

- pandas  
- numpy  
- matplotlib  
- scipy  

```bash
pip install pandas numpy matplotlib scipy
