# 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city not in cache:
            cache.append(city)
            if cacheSize < len(cache):
                answer += 5
                cache.pop(0)
            elif len(cache) <= cacheSize:
                answer += 5
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)
    return answer

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))