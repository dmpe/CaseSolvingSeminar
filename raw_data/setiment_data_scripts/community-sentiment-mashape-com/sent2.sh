# Taken from https://github.com/Charudatt89/Personality_Recognition/blob/master/22-9-PersonalityRecognition/SourceCode/FEATURE_BASED_APPROACH/ source_code/run_sentiment_8.sh

file=data.csv
while IFS= read -r line
do
        # echo line is stored in $line
	tmp=`curl -d "txt=$line" https://community-sentiment.p.mashape.com/text/ -H "X-Mashape-Key: Gkqp1Q0amCmsh2nUi5qabMR97LY2p1eXbQjjsnEEvzsCQmyU15" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json" `
	echo $tmp >> result2.json
	echo "-----------------"
done < "$file"
echo "-----------------------"
#echo $tmp
echo "--------"
