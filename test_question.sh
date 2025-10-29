#!/bin/bash
# Test rapide d'une question au Rav

echo "🕎 Torah AI - Test d'une question"
echo ""
echo "Posez votre question (ou appuyez sur Entrée pour la question par défaut) :"
read QUESTION

if [ -z "$QUESTION" ]; then
    QUESTION="Quelle est la signification du Shabbat dans la Kabbale?"
fi

echo ""
echo "Envoi de la question : $QUESTION"
echo ""

curl -s -X POST http://localhost:8000/api/v1/question \
  -H "Content-Type: application/json" \
  -d "{
    \"question\": \"$QUESTION\",
    \"langue\": \"fr\",
    \"niveau\": \"intermediaire\"
  }" | python3 -m json.tool

echo ""
