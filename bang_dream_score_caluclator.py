def note_score_calculate(difficulty, notes, deck_power):
    difficulty_bonus = ((int(difficulty) - 5) * 0.01) + 1
    notes_combo_bonus = 0
    notes = int(notes)
    deck_power = int(deck_power)
    if notes <= 20:
        notes_combo_bonus = 1
    elif notes > 20 and notes < 50:
        notes_combo_bonus = 1.01
    elif notes > 50 and notes < 100:
        notes_combo_bonus = 1.02
    elif notes > 100 and notes < 300:
        notes_combo_bonus = 1 + (notes // 50)
    elif notes > 301:
        notes_combo_bonus = 1.07 + ((notes - 301) // 100)

    note_score = deck_power * 3 * difficulty_bonus / notes * 1.1 * notes_combo_bonus
    print(note_score)
    note_score1 = round(note_score)
    return note_score1

def total_score_calculate(notes, note_score):
    notes = int(notes)
    expect_score = note_score * notes
    expect_score1 = round(int(expect_score))
    return expect_score1

if __name__ == '__main__':
    main()


#노트 스코어 = 286860×3×((27-5)×0.01+1)÷853×1.1×1.12 1.22

#난이도 27렙 노트 853개 종합력 286860