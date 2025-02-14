from collections import defaultdict

test_num = int(input())
for _ in range(test_num):
    team_num = int(input())
    case = list(map(int, input().split()))

    valid_team = {t for t in case if case.count(t) == 6}
    case = [c for c in case if c in valid_team]
    
    teams = defaultdict(list)
    for i, team in enumerate(case, start=1):
        teams[team].append(i)

    team_scores = {team: sum(ranks[:4]) for team, ranks in teams.items()}
    min_score = min(team_scores.values())
    winners = [team for team, score in team_scores.items() if score==min_score]
    
    if len(winners) > 1:
        winner = min(winners, key=lambda team: teams[team][4])
    else:
        winner = winners[0]
    print(winner)