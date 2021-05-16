import xml.etree.ElementTree as et
import json

class Converter:
    def __init__(self):
        self.output_data = []
        self.polarity_dict = {
            "neutral": 0,
            "positive": 1,
            "negative": -1,
            "conflict": 2,
            "none": 3
        }
        self.aspect = {
            "service": 1,
            "food": 2,
            "anecdotes/miscellaneous": 3,
            "price": 4,
            "ambience": 5
        }


    def convert(self, training_path):
        xtree = et.parse(training_path)
        xroot = xtree.getroot()
        categories_id = 1;
        terms_id = 1;

        for sentence in xroot.findall("sentence"):

            text = sentence.find('text').text
            category_arr = []
            category_tracker = []
            newaspectCategory = []

            #aspects
            for aspectCategory in sentence.findall("./aspectCategories/aspectCategory"):
                newaspectCategory = aspectCategory.attrib

                # if newaspectCategory['polarity'] not in self.polarity_dict:
                #     continue

                # Add new category into aspect dict
                # if aspectCategory['category'] not in self.aspect:
                #     self.aspect[aspectCategory['category']] = categories_id
                #     categories_id += 1

                # Add aspect into data

                newaspectCategory['polarity_id'] = self.polarity_dict[newaspectCategory['polarity']]
                newaspectCategory['category_id'] = self.aspect[newaspectCategory['category']]
                category_arr.append(newaspectCategory.copy())
                category_tracker.append(newaspectCategory['category'])

            # for aspect_term in sentence.findall("./aspectTerms/aspectTerm"):
            #     aspect_term = aspect_term.attrib
            #
            #     if aspect_term['polarity'] not in self.polarity_dict:
            #         continue
            #
            #     if 'from' in aspect_term:
            #         del aspect_term['from']
            #
            #     if 'to' in aspect_term:
            #         del aspect_term['to']
            #
            #     aspect_term['polarity_id'] = self.polarity_dict[aspect_term['polarity']]
            #     terms_arr.append(aspect_term)

            if 'price' not in category_tracker:
                newaspectCategory['polarity_id'] = self.polarity_dict['none']
                newaspectCategory['category_id'] = self.aspect['price']
                newaspectCategory['polarity'] = "none"
                newaspectCategory['category'] = "price"
                category_arr.append(newaspectCategory.copy())

            if 'food' not in category_tracker:
                newaspectCategory['polarity_id'] = self.polarity_dict['none']
                newaspectCategory['category_id'] = self.aspect['food']
                newaspectCategory['polarity'] = "none"
                newaspectCategory['category'] = "food"
                category_arr.append(newaspectCategory.copy())

            if 'service' not in category_tracker:
                newaspectCategory['polarity_id'] = self.polarity_dict['none']
                newaspectCategory['category_id'] = self.aspect['service']
                newaspectCategory['polarity'] = "none"
                newaspectCategory['category'] = "service"
                category_arr.append(newaspectCategory.copy())

            if 'anecdotes/miscellaneous' not in category_tracker:
                newaspectCategory['polarity_id'] = self.polarity_dict['none']
                newaspectCategory['category_id'] = self.aspect['anecdotes/miscellaneous']
                newaspectCategory['polarity'] = "none"
                newaspectCategory['category'] = "anecdotes/miscellaneous"
                category_arr.append(newaspectCategory.copy())

            if 'ambience' not in category_tracker:
                newaspectCategory['polarity_id'] = self.polarity_dict['none']
                newaspectCategory['category_id'] = self.aspect['ambience']
                newaspectCategory['polarity'] = "none"
                newaspectCategory['category'] = "ambience"
                category_arr.append(newaspectCategory.copy())

            self.output_data.append({
                "text": text,
                "categories": category_arr
            })

    def generateJson(self, file):

        final_output = {
            "polarity_library": self.polarity_dict,
            "data": self.output_data,
            "aspect_library": self.aspect
        }

        print(final_output)

        with open(file, 'w') as fp:
            json.dump(final_output, fp, indent=4)
            fp.close()




if __name__ == '__main__':
    TRAINING_DATA_PATH = 'Restaurants_Train.xml'
    TESTING_DATA_PATH = 'Restaurants_Test_Gold.xml'

    converter = Converter()
    converter.convert(TRAINING_DATA_PATH)
    converter.generateJson('Restaurants_Original_Train.json')
    # converter.generateJson('./datasets/semeval14/Restaurants_Train.json')

    converter = Converter()
    converter.convert(TESTING_DATA_PATH)
    converter.generateJson('Restaurants_Original_Test.json')
    # converter.generateJson('./datasets/semeval14/Restaurants_Test.json')