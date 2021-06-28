"""

리듬게임 뱅드림의 예상 점수를 나타냅니다. 100% ALL PERFECT, 스킬 발동 X 기준입니다.

"""
def note_score_calculate(difficulty, notes, deck_power):
     # 난이도 보너스를 구합니다. 난이도 보너스 = (난이도 - 5) * 0.01 + 1
    difficulty_bonus = ((difficulty - 5) * 0.01) + 1
     # 노트 콤보 보너스는 노트 갯수에 따라 다르기때문에 따로 분류를 해놓았습니다.
    notes_combo_bonus = 0
     # 노트 콤보 보너스 기존 1배 / 20 ~ 50 1.01 / 51 ~ 100 1.02 / 101부터는 50개의 노트당 0.01씩 추가 / 301부터는 100개의 노트당 0.01씩 추가
    if notes <= 20:
        notes_combo_bonus = 1
    elif notes > 20 and notes < 50:
        notes_combo_bonus = 1.01
    elif notes > 50 and notes < 100:
        notes_combo_bonus = 1.02
    elif notes > 100 and notes < 300:
        notes_combo_bonus = 1 + (notes // 50)
    elif notes > 301:
        notes_combo_bonus = 1.07 + (0.01 * ((notes - 301) // 100))
    else:
         #첫 기본 노트 콤보 스코어는 1배이므로 1배로 설정
        notes_combo_bonus = 1
     # 방도리 스코어 공식 = 종합력 * 3 * 난이도 보너스 / 노트 갯수 * 1.1(퍼펙트 판정 보너스) * 노트 콤보 배율 보너스 * 스킬 스코어 보너스
    note_score = deck_power * 3 * difficulty_bonus / notes * 1.1 * notes_combo_bonus
     # 노트 개당 숫자가 소숫점 몇십자리까지 나오기 때문에 반올림을 해주었습니다.
    note_score = round(note_score)
    return note_score

 # 총 스코어의 합계를 구합니다. 혹시 노트당 점수를 따로 쓸 수 있지 않을까? 싶어서 따로 떼놓았습니다.
def total_score_calculate(notes, note_score):
    # 예상점수 노트당 스코어 * 노트 갯수
    expect_score = note_score * notes
    # 노트당 스코어에서 소숫점이 나올 수도 있으니 쓸데없는 코드 낭비 (?)
    expect_score = round(expect_score)
    return expect_score

if __name__ == '__main__':
    main()
