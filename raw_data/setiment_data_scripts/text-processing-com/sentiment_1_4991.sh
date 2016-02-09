# Taken from https://github.com/Charudatt89/Personality_Recognition/blob/master/22-9-PersonalityRecognition/SourceCode/FEATURE_BASED_APPROACH/ source_code/run_sentiment_8.sh

file=data.csv
while IFS= read -r line
do
        # echo line is stored in $line
	tmp=`curl -d "text=$line" http://text-processing.com/api/sentiment/`
	echo $tmp >> result.csv
	echo "-----------------"
done < "$file"
echo "-----------------------"
#echo $tmp
echo "--------"
