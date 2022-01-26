import json

def phrasel_search(P, Queries):
    ans = []
    for query in Queries:
        matches = []
        query_list = query.split()
        for phrase in P:
            phrase_list = phrase.split()
            for i, word in enumerate(query_list):
                skip = False
                if word == phrase_list[0]:
                    p_index = 0
                    q_index = i
                    while True:
                        if phrase_list[p_index] == query_list[q_index] and p_index == len(phrase_list) - 1 and q_index == len(query_list) - 1:
                            matches.append(' '.join(query_list[i:]))
                            break
                        elif phrase_list[p_index] == query_list[q_index] and p_index == len(phrase_list) - 1:
                            matches.append(' '.join(query_list[i:q_index + 1]))
                            break
                        elif phrase_list[p_index] == query_list[q_index]:
                            p_index += 1
                            q_index += 1
                        elif  q_index != len(query_list) - 1 and phrase_list[p_index] == query_list[q_index + 1] and not skip:
                            skip = True
                            q_index += 1
                        else:
                            break
        ans.append(matches)        
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')

'''
tests = ['sample.json', '20_points.json', '30_points.json', '50_points.json']

if __name__ == "__main__":
    all_pass = True
    for test in tests:
        with open(test, 'r') as f:
            print(test)
            sample_data = json.loads(f.read())
            P, Queries = sample_data['phrases'], sample_data['queries']
            returned_ans = phrasel_search(P, Queries)
            for i in range(len(Queries)):
                if sorted(returned_ans[i]) != sorted(sample_data['solution'][i]):
                    all_pass = False
                    print(f'query #{i}\nreturned answer: {sorted(returned_ans[i])}\nexpected answer: {sorted(sample_data["solution"][i])}')
    if all_pass:
        print('All tests passed!')
'''