import json
class Solution(object):
    """
    :rtype: int
    """
    # loading records from json file into object
    def fetchRecordsFromJson(self):
        with open("details.json") as file:
            personalData = json.load(file)
        return personalData
    # method to calculate BMI and updating person's records with BMI, BMI Category, HealthRisk
    def calculateBMI(self, personalData):
        OverweightPersons = 0
        if(len(personalData)!=0):
            for record in personalData:
                BMI = (record['WeightKg']) /((record['HeightCm']/100)**2)
                if(BMI <= 18.4):
                    BMICategory = "Underweight"
                    HealthStatus = "Malnutrition risk"
                elif(BMI >= 18.5 and BMI <= 24.9):
                    BMICategory = "Normal weight"
                    HealthStatus = "Low risk"
                elif(BMI >= 25 and BMI <= 29.9):
                    BMICategory = "Overweight"
                    HealthStatus = "Enhanced risk"
                elif(BMI >= 30 and BMI <= 34.9):
                    BMICategory = "Moderately obese"
                    HealthStatus = "Medium risk"
                elif(BMI >= 35 and BMI <= 39.9):
                    BMICategory = "Severely obese"
                    HealthStatus = "High risk"
                elif(BMI >= 40):
                    BMICategory = "Very severely obese"
                    HealthStatus = "Very high risk"
                record.update(
                    {'BMI': BMI, 'BMICategory': BMICategory, 'HealthRisk': HealthStatus})
                if(BMICategory == "Overweight" or BMICategory == "Moderately obese" or BMICategory == "Severely obese" or BMICategory == "Very severely obese"):
                    OverweightPersons = OverweightPersons+1
        else:
            return 'No Records Found'
        return personalData


if __name__ == '__main__':
    response = Solution()
    personalData = response.fetchRecordsFromJson()
    response.calculateBMI(personalData)
