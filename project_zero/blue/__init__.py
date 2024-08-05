from otree.api import *
import json
import random
import openai

CHATGPT_KEY = 'XXXXXXX'

def runGPT(inputMessage):
    openai.api_key = CHATGPT_KEY
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            messages=inputMessage,
            temperature=1.0
        )
        return completion.choices[0].message.content
    except Exception as e:
        print("Error in runGPT:", e)
        return "Sorry, something went wrong."

class C(BaseConstants):
    NAME_IN_URL = "blue"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    my_task_assignment = models.IntegerField(initial=0)
    my_politeness_assignment = models.IntegerField(initial=0)

    conversation_history_ek = models.LongStringField(initial=json.dumps([]))
    conversation_history_do = models.LongStringField(initial=json.dumps([]))

    answer1 = models.LongStringField(label="Your message for the account's department:")
    answer2 = models.LongStringField(label="Your shopping list:")

    educational_level = models.StringField(
        choices=[['Bachelors Degree', 'Bachelors Degree'], ['Masters Degree', 'Masters Degree'],
                 ['Doctorate Degree', 'Doctorate Degree'], ['Other', 'Other'], ],
        label='What is your current education program type?',
    )
    age = models.StringField(
        choices=[
            ['16-19', '16-19'],
            ['20-24', '20-24'],
            ['25-28', '25-28'],
            ['29-32', '29-32'],
            ['32+', '32+']
        ],
        label='What is your age?',
        widget=widgets.RadioSelect,
    )
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Non-binary', 'Non-binary'], ['Other', 'Other'],
                 ['Prefer Not To Say', 'Prefer Not To Say']],
        label='What is your Gender?',
    )

    q1_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The chatbot was easy to use.',
        widget=widgets.RadioSelectHorizontal,
    )
    q1_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The chatbot was easy to use.',
        widget=widgets.RadioSelectHorizontal,
    )
    q2_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The information provided by the chatbot was easy to understand.',
        widget=widgets.RadioSelectHorizontal,
    )
    q2_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The information provided by the chatbot was easy to understand.',
        widget=widgets.RadioSelectHorizontal,
    )
    q3_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The recommendations were relevant to the task.',
        widget=widgets.RadioSelectHorizontal,
    )
    q3_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The recommendations were relevant to the task.',
        widget=widgets.RadioSelectHorizontal,
    )
    q4_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The chatbot provided personalized responses.',
        widget=widgets.RadioSelectHorizontal,
    )
    q4_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The chatbot provided personalized responses.',
        widget=widgets.RadioSelectHorizontal,
    )
    q5_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='Using the chatbot saved me time in finding products.',
        widget=widgets.RadioSelectHorizontal,
    )
    q5_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='Using the chatbot saved me time in finding products.',
        widget=widgets.RadioSelectHorizontal,
    )
    q6_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The chatbot reduced my effort in searching for products.',
        widget=widgets.RadioSelectHorizontal,
    )
    q6_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='The chatbot reduced my effort in searching for products.',
        widget=widgets.RadioSelectHorizontal,
    )
    q7_1 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='For similar tasks in the future. I would recommend using this product recommendation chatbot.',
        widget=widgets.RadioSelectHorizontal,
    )
    q7_2 = models.StringField(
        choices=[
            ['1', 'Strongly Disagree'],
            ['2', 'Disagree'],
            ['3', 'Neutral'],
            ['4', 'Agree'],
            ['5', 'Strongly Agree']
        ],
        label='For similar tasks in the future. I would recommend using this product recommendation chatbot.',
        widget=widgets.RadioSelectHorizontal,
    )



class ChatbotEk(Page):
    form_model = 'player'
    form_fields = ['answer1']

    def live_method(player, data):
        conversation_history_ek = player.field_maybe_none('conversation_history_ek')
        if isinstance(data, str):
            history = json.loads(conversation_history_ek)
            user_message = {"role": "user", "content": data}
            history.append(user_message)

            summary = []
            for entry in history:
                if entry['role'] == 'user':
                    summary.append(f"User said: {entry['content']}")
                elif entry['role'] == 'assistant':
                    summary.append(f"Assistant replied: {entry['content']}")
            summary_text = " Then ".join(summary)
            # print(player.my_politeness_assignment)
            if (player.my_politeness_assignment == 1):
                system_prompt_text = (
                    "You are a product recommendation assistant on the DP skincare website. Your task is to answer their question. If they ask about any products, answer it from the PRODUCT LIST. You can only recommend products from the store’s product list. Do not name any other brand or products from the internet. If the user asks you about a product's price or availability, use the PRODUCT LIST. All your responses should be one or two line sentences and helpful to them."
                    "PRODUCT LIST: DP Sunscreen Lotion SPF 50 - Description: Our broad-spectrum Sunscreen Lotion with SPF 50 offers superior protection against UVA and UVB rays, making it an essential for sunny weather. Key ingredients include zinc oxide, titanium dioxide, aloe vera, and vitamin E. To use, apply generously 15 minutes before sun exposure and reapply every 2 hours or after swimming or sweating. Quantity: 100ml Price: €25 DP Hydrating Facial Mist - Description: The Hydrating Facial Mist refreshes and revitalizes your skin with its blend of hyaluronic acid, rose water, and chamomile extract. Suitable for all skin types, it can be used throughout the day by simply spraying on the face and neck as needed. Quantity: 50ml Price: €15 DP Aloe Vera Gel - Description: This soothing Aloe Vera Gel is perfect for calming and hydrating the skin after sun exposure. It contains pure aloe vera extract, glycerin, and green tea extract. Apply generously to the affected areas on both the face and body for a cooling effect. Quantity: 100ml Price: €12 DP Lightweight Moisturizer - Description: Our Lightweight Moisturizer provides long-lasting hydration without clogging pores. Formulated with squalane, glycerin, and niacinamide, it keeps your skin supple and smooth. Use it on clean skin in the morning and evening for best results. Quantity: 50ml Price: €20 DP Vitamin C Serum - Description: The Vitamin C Serum brightens the skin and reduces dark spots with its potent blend of vitamin C, ferulic acid, and hyaluronic acid. Apply a few drops to clean, dry skin before moisturizing in the morning to enhance your complexion. Quantity: 30ml Price: €30 DP Daily Face Cleanser - Description: Our gentle Daily Face Cleanser effectively removes impurities without drying out your skin. With salicylic acid, chamomile extract, and glycerin, it’s ideal for daily use. Apply to wet skin, massage gently, and rinse thoroughly. Quantity: 100ml Price: €18 DP Night Repair Cream - Description: The Night Repair Cream rejuvenates your skin overnight with a rich blend of retinol, peptides, and hyaluronic acid. Apply to clean skin at night, avoiding the eye area, to wake up with refreshed and revitalized skin. Quantity: 50ml Price: €35 DP Lip Balm with SPF 15 - Description: Protect and moisturize your lips with our Lip Balm, which includes SPF 15 for sun protection. Key ingredients like shea butter and beeswax keep your lips soft and hydrated. Apply as needed, especially after eating or drinking. Quantity: 10ml Price: €10"
                    "All your messages should be as polite as they can be. Apologise when needed, ask follow-up questions based on their previous message (only when applicable), and make them feel cared for. This is the previous conversation history: ")
            else:
                system_prompt_text = (
                    "You are a product recommendation assistant on the DP skincare website. Your task is to answer their question. If they ask about any products, answer it from the PRODUCT LIST. You can only recommend products from the store’s product list. Do not name any other brand or products from the internet. If the user asks you about a product's price or availability, use the PRODUCT LIST. All your responses should be one or two line sentences and helpful to them."
                    "PRODUCT LIST: DP Sunscreen Lotion SPF 50 - Description: Our broad-spectrum Sunscreen Lotion with SPF 50 offers superior protection against UVA and UVB rays, making it an essential for sunny weather. Key ingredients include zinc oxide, titanium dioxide, aloe vera, and vitamin E. To use, apply generously 15 minutes before sun exposure and reapply every 2 hours or after swimming or sweating. Quantity: 100ml Price: €25 DP Hydrating Facial Mist - Description: The Hydrating Facial Mist refreshes and revitalizes your skin with its blend of hyaluronic acid, rose water, and chamomile extract. Suitable for all skin types, it can be used throughout the day by simply spraying on the face and neck as needed. Quantity: 50ml Price: €15 DP Aloe Vera Gel - Description: This soothing Aloe Vera Gel is perfect for calming and hydrating the skin after sun exposure. It contains pure aloe vera extract, glycerin, and green tea extract. Apply generously to the affected areas on both the face and body for a cooling effect. Quantity: 100ml Price: €12 DP Lightweight Moisturizer - Description: Our Lightweight Moisturizer provides long-lasting hydration without clogging pores. Formulated with squalane, glycerin, and niacinamide, it keeps your skin supple and smooth. Use it on clean skin in the morning and evening for best results. Quantity: 50ml Price: €20 DP Vitamin C Serum - Description: The Vitamin C Serum brightens the skin and reduces dark spots with its potent blend of vitamin C, ferulic acid, and hyaluronic acid. Apply a few drops to clean, dry skin before moisturizing in the morning to enhance your complexion. Quantity: 30ml Price: €30 DP Daily Face Cleanser - Description: Our gentle Daily Face Cleanser effectively removes impurities without drying out your skin. With salicylic acid, chamomile extract, and glycerin, it’s ideal for daily use. Apply to wet skin, massage gently, and rinse thoroughly. Quantity: 100ml Price: €18 DP Night Repair Cream - Description: The Night Repair Cream rejuvenates your skin overnight with a rich blend of retinol, peptides, and hyaluronic acid. Apply to clean skin at night, avoiding the eye area, to wake up with refreshed and revitalized skin. Quantity: 50ml Price: €35 DP Lip Balm with SPF 15 - Description: Protect and moisturize your lips with our Lip Balm, which includes SPF 15 for sun protection. Key ingredients like shea butter and beeswax keep your lips soft and hydrated. Apply as needed, especially after eating or drinking. Quantity: 10ml Price: €10"
                    "This is the previous conversation history: ")


            response_content = runGPT([{'role': 'user', 'content': data}, {'role': 'system', 'content': system_prompt_text + summary_text}])

            assistant_message = {"role": "assistant", "content": response_content}
            history.append(assistant_message)

            player.conversation_history_ek = json.dumps(history)
            return {player.id_in_group: [True, response_content]}

    def vars_for_template(player):
        if player.my_task_assignment == 1:
            title = "Mr. Johnson's note for you:"
            the_note = "Sunscreen min SPF 50, something for my oily skin, and my wife's dry skin. Also, Night mist and something for her night routine. Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products."
        else:
            title = "Information about the city:"
            the_note = "<b>Climate:</b> Typically dry with significant air pollution.<br/><b>Common Pollutants:</b> PM2.5, PM10, ozone, nitrogen dioxide.<br/><b>Skin Concerns:</b> Dryness, irritation, clogged pores, sensitivity. <br/><br/>Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products."
        return {'title': title, 'the_note': the_note}


class ChatbotDo(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def live_method(player, data):
        conversation_history_do = player.field_maybe_none('conversation_history_do')
        if isinstance(data, str):
            history = json.loads(conversation_history_do)
            user_message = {"role": "user", "content": data}
            history.append(user_message)

            summary = []
            for entry in history:
                if entry['role'] == 'user':
                    summary.append(f"User said: {entry['content']}")
                elif entry['role'] == 'assistant':
                    summary.append(f"Assistant replied: {entry['content']}")
            summary_text = " Then ".join(summary)
            # print(player.my_assignment)
            if(player.my_politeness_assignment == 1):
                system_prompt_text = ("You are a product recommendation assistant on the DP skincare website. Your task is to answer their question. If they ask about any products, answer it from the PRODUCT LIST. You can only recommend products from the store’s product list. Do not name any other brand or products from the internet. If the user asks you about a product's price or availability, use the PRODUCT LIST. All your responses should be one or two line sentences and helpful to them."
                                      "PRODUCT LIST: DP Sunscreen Lotion SPF 50 - Description: Our broad-spectrum Sunscreen Lotion with SPF 50 offers superior protection against UVA and UVB rays, making it an essential for sunny weather. Key ingredients include zinc oxide, titanium dioxide, aloe vera, and vitamin E. To use, apply generously 15 minutes before sun exposure and reapply every 2 hours or after swimming or sweating. Quantity: 100ml Price: €25 DP Hydrating Facial Mist - Description: The Hydrating Facial Mist refreshes and revitalizes your skin with its blend of hyaluronic acid, rose water, and chamomile extract. Suitable for all skin types, it can be used throughout the day by simply spraying on the face and neck as needed. Quantity: 50ml Price: €15 DP Aloe Vera Gel - Description: This soothing Aloe Vera Gel is perfect for calming and hydrating the skin after sun exposure. It contains pure aloe vera extract, glycerin, and green tea extract. Apply generously to the affected areas on both the face and body for a cooling effect. Quantity: 100ml Price: €12 DP Lightweight Moisturizer - Description: Our Lightweight Moisturizer provides long-lasting hydration without clogging pores. Formulated with squalane, glycerin, and niacinamide, it keeps your skin supple and smooth. Use it on clean skin in the morning and evening for best results. Quantity: 50ml Price: €20 DP Vitamin C Serum - Description: The Vitamin C Serum brightens the skin and reduces dark spots with its potent blend of vitamin C, ferulic acid, and hyaluronic acid. Apply a few drops to clean, dry skin before moisturizing in the morning to enhance your complexion. Quantity: 30ml Price: €30 DP Daily Face Cleanser - Description: Our gentle Daily Face Cleanser effectively removes impurities without drying out your skin. With salicylic acid, chamomile extract, and glycerin, it’s ideal for daily use. Apply to wet skin, massage gently, and rinse thoroughly. Quantity: 100ml Price: €18 DP Night Repair Cream - Description: The Night Repair Cream rejuvenates your skin overnight with a rich blend of retinol, peptides, and hyaluronic acid. Apply to clean skin at night, avoiding the eye area, to wake up with refreshed and revitalized skin. Quantity: 50ml Price: €35 DP Lip Balm with SPF 15 - Description: Protect and moisturize your lips with our Lip Balm, which includes SPF 15 for sun protection. Key ingredients like shea butter and beeswax keep your lips soft and hydrated. Apply as needed, especially after eating or drinking. Quantity: 10ml Price: €10"
                                      "All your messages should be as polite as they can be. Apologise when needed, ask follow-up questions based on their previous message (only when applicable), and make them feel cared for. This is the previous conversation history: ")
            else:
                system_prompt_text = ("You are a product recommendation assistant on the DP skincare website. Your task is to answer their question. If they ask about any products, answer it from the PRODUCT LIST. You can only recommend products from the store’s product list. Do not name any other brand or products from the internet. If the user asks you about a product's price or availability, use the PRODUCT LIST. All your responses should be one or two line sentences and helpful to them."
                                      "PRODUCT LIST: DP Sunscreen Lotion SPF 50 - Description: Our broad-spectrum Sunscreen Lotion with SPF 50 offers superior protection against UVA and UVB rays, making it an essential for sunny weather. Key ingredients include zinc oxide, titanium dioxide, aloe vera, and vitamin E. To use, apply generously 15 minutes before sun exposure and reapply every 2 hours or after swimming or sweating. Quantity: 100ml Price: €25 DP Hydrating Facial Mist - Description: The Hydrating Facial Mist refreshes and revitalizes your skin with its blend of hyaluronic acid, rose water, and chamomile extract. Suitable for all skin types, it can be used throughout the day by simply spraying on the face and neck as needed. Quantity: 50ml Price: €15 DP Aloe Vera Gel - Description: This soothing Aloe Vera Gel is perfect for calming and hydrating the skin after sun exposure. It contains pure aloe vera extract, glycerin, and green tea extract. Apply generously to the affected areas on both the face and body for a cooling effect. Quantity: 100ml Price: €12 DP Lightweight Moisturizer - Description: Our Lightweight Moisturizer provides long-lasting hydration without clogging pores. Formulated with squalane, glycerin, and niacinamide, it keeps your skin supple and smooth. Use it on clean skin in the morning and evening for best results. Quantity: 50ml Price: €20 DP Vitamin C Serum - Description: The Vitamin C Serum brightens the skin and reduces dark spots with its potent blend of vitamin C, ferulic acid, and hyaluronic acid. Apply a few drops to clean, dry skin before moisturizing in the morning to enhance your complexion. Quantity: 30ml Price: €30 DP Daily Face Cleanser - Description: Our gentle Daily Face Cleanser effectively removes impurities without drying out your skin. With salicylic acid, chamomile extract, and glycerin, it’s ideal for daily use. Apply to wet skin, massage gently, and rinse thoroughly. Quantity: 100ml Price: €18 DP Night Repair Cream - Description: The Night Repair Cream rejuvenates your skin overnight with a rich blend of retinol, peptides, and hyaluronic acid. Apply to clean skin at night, avoiding the eye area, to wake up with refreshed and revitalized skin. Quantity: 50ml Price: €35 DP Lip Balm with SPF 15 - Description: Protect and moisturize your lips with our Lip Balm, which includes SPF 15 for sun protection. Key ingredients like shea butter and beeswax keep your lips soft and hydrated. Apply as needed, especially after eating or drinking. Quantity: 10ml Price: €10"
                                      "This is the previous conversation history: ")

            response_content = runGPT([{'role': 'user', 'content': data}, {'role': 'system', 'content': system_prompt_text + summary_text}])

            assistant_message = {"role": "assistant", "content": response_content}
            history.append(assistant_message)

            player.conversation_history_do = json.dumps(history)
            return {player.id_in_group: [True, response_content]}

    def vars_for_template(player):
        if player.my_task_assignment == 2:
            title = "Mr. Johnson's note for you:"
            the_note = "Sunscreen min SPF 50, something for my oily skin, and my wife's dry skin. Also, Night mist and something for her night routine. Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products."
        else:
            title = "Information about the city:"
            the_note = "<b>Climate:</b> Typically dry with significant air pollution.<br/><b>Common Pollutants:</b> PM2.5, PM10, ozone, nitrogen dioxide.<br/><b>Skin Concerns:</b> Dryness, irritation, clogged pores, sensitivity. <br/><br/>Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products."
        return {'title': title, 'the_note': the_note}

class QuestionsEk(Page):
    form_model = 'player'
    form_fields = ['q1_1','q2_1','q3_1','q4_1','q5_1','q6_1','q7_1']

class QuestionsDo(Page):
    form_model = 'player'
    form_fields = ['q1_2','q2_2','q3_2','q4_2','q5_2','q6_2','q7_2']

class Questions(Page):
    form_model = 'player'
    form_fields = ['age','gender','educational_level']

class ScenarioEk(Page):
    @staticmethod
    def vars_for_template(player):
        random_number = random.randint(1, 100)
        if random_number % 2 == 0:
            situation = "Your boss, Mr. Johnson, is going on a vacation to Spain with his wife. He has asked you to buy skincare products for their trip. You need to interact with an AI chatbot to find the suitable products for the trip. After selecting the products, you need to create a price list and send it to the accounts department for reimbursement."
            the_note = "He left a note for you: Sunscreen min SPF 50, something for my oily skin, and my wife's dry skin. Also, Night mist and something for her night routine. Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products."
            player.my_task_assignment = 1 # Spain Task
        else:
            situation = "Your partner is travelling to a polluted city for a week long business trip. Your task is to make sure that your partner has the best skincare products to protect their skin from the polluted environment. On the next page, you need to prepare a shopping list along with their prices. You will use a product recommendation AI chatbot from a skincare online store for your task."
            the_note = "Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products.<br/><br/>Here is what you found out, about the city: <br/><br/><b>Climate:</b> Typically dry with significant air pollution.<br/><b>Common Pollutants:</b> PM2.5, PM10, ozone, nitrogen dioxide.<br/><b>Skin Concerns:</b> Dryness, irritation, clogged pores, sensitivity."
            player.my_task_assignment = 2  # Business Task
        return {'situation': situation, 'the_note': the_note}

    def before_next_page(player, timeout_happened):
        random_number = random.randint(1, 100)
        if random_number % 2 == 0:
            player.my_politeness_assignment = 1 # Polite Version First
        else:
            player.my_politeness_assignment = 2 # Neutral Version First


class ScenarioDo(Page):
    @staticmethod
    def vars_for_template(player):
        if player.my_task_assignment == 2:
            situation = "Your boss, Mr. Johnson, is going on a vacation to Spain with his wife. He has asked you to buy skincare products for their trip. You need to interact with an AI chatbot to find the suitable products for the trip. After selecting the products, you need to create a price list and send it to the accounts department for reimbursement."
            the_note = "He left a note for you: Sunscreen min SPF 50, something for my oily skin, and my wife's dry skin. Also, Night mist and something for her night routine. Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products."
        else:
            situation = "Your partner is travelling to a polluted city for a week long business trip. Your task is to make sure that your partner has the best skincare products to protect their skin from the polluted environment. On the next page, you need to prepare a shopping list along with their prices. You will use a product recommendation AI chatbot from a skincare online store for your task."
            the_note = "Make sure to check that everything you select has 100ml or less to comply with air travel regulations. Your total budget is 120 € and you can select a maximum of four products.<br/><br/>Here is what you found out, about the city: <br/><br/><b>Climate:</b> Typically dry with significant air pollution.<br/><b>Common Pollutants:</b> PM2.5, PM10, ozone, nitrogen dioxide.<br/><b>Skin Concerns:</b> Dryness, irritation, clogged pores, sensitivity."
        return {'situation': situation, 'the_note': the_note}

    def before_next_page(player, timeout_happened):
        if player.my_politeness_assignment == 1:
            player.my_politeness_assignment = 2  # Polite Version Was First
        else:
            player.my_politeness_assignment = 1

class ThankYou(Page):
    pass

page_sequence = [ScenarioEk, ChatbotEk, QuestionsEk, ScenarioDo, ChatbotDo, QuestionsDo, Questions, ThankYou]
