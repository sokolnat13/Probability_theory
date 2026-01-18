import numpy as np

def friendship_paradox_check(friends_dict):
    results = \
    {
        'total_people': len(friends_dict),
        'avg_friends': 0,
        'avg_friends_of_friends': 0,
    }

    friend_counts = {person: len(friends) for person, friends in friends_dict.items()}
    results['avg_friends'] = np.mean(list(friend_counts.values()))
    avg_friends_of_friends_list = []

    for person, friends in friends_dict.items():
        if friends:
            friends_friend_counts = [friend_counts[friend] for friend in friends]
            avg_friends_of_friends_list.append(np.mean(friends_friend_counts))
        else:
            avg_friends_of_friends_list.append(0)

    results['avg_friends_of_friends'] = np.mean(avg_friends_of_friends_list)

    return results

if __name__ == "__main__":
    friends = \
    {
        'Андрей': ['Семён', 'Нина', 'Виктор', 'Виталя'],
        'Ольга': ['Нина', 'Оксана', 'Елена', 'Дарья', 'Валерий', 'Виталя'],
        'Семён': ['Андрей', 'Виктор', 'Тамара'],
        'Нина': ['Ольга', 'Андрей', 'Елена'],
        'Оксана': ['Ольга','Генадий', 'Виктор'],
        'Генадий': ['Оксана','Виктор'],
        'Елена': ['Ольга', 'Нина', 'Виктор'],
        'Виктор': ['Андрей', 'Семён', 'Оксана', 'Генадий', 'Елена', 'Тамара', 'Аркадий'],
        'Аркадий': ['Виктор', 'Виталя'],
        'Тамара': ['Виктор', 'Дарья', 'Валерий'],
        'Валерий': ['Тамара', 'Ольга'],
        'Виталя': ['Андрей', 'Аркадий', 'Ольга'],
        'Дарья': ['Тамара', 'Ольга']
    }

    results = friendship_paradox_check(friends)

    print(f"Парадокс дружбы (friendship paradox) — феномен, состоящий в том, что, как правило, у большинства людей друзей меньше, чем в среднем у их друзей")
    print(f"Всего людей: {results['total_people']}")
    print(f"Среднее количество друзей (у 1 человечка): {results['avg_friends']:.3f}")
    print(f"Среднее количество друзей у друзей: {results['avg_friends_of_friends']:.3f}")
