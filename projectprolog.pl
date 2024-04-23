default_gpa(2.2).

% Calculate grade points earned for each module
grade_points(Module, Semester, GradePoints) :-
    grade(Module, Semester, Grade),
    credit(Module, Credit),
    GradePoints is Grade * Credit.

% Calculate total grade points and total credits for a semester
semester_totals(Semester, TotalGradePoints, TotalCredits) :-
    findall(GradePoints, grade_points(_, Semester, GradePoints), GradePointsList),
    sum_list(GradePointsList, TotalGradePoints),
    findall(Credit, (grade(Module, Semester, _), credit(Module, Credit)), CreditsList),
    sum_list(CreditsList, TotalCredits).

% Calculate GPA for a semester
gpa(Semester, GPA) :-
    (semester_totals(Semester, TotalGradePoints, TotalCredits) ->
        GPA is TotalGradePoints / TotalCredits
    ;
        default_gpa(GPA)
    ).

% Calculate cumulative GPA for two semesters
cumulative_gpa(Semester1, Semester2, CumulativeGPA) :-
    semester_totals(Semester1, TotalGradePoints1, TotalCredits1),
    semester_totals(Semester2, TotalGradePoints2, TotalCredits2),
    TotalGradePoints is TotalGradePoints1 + TotalGradePoints2,
    TotalCredits is TotalCredits1 + TotalCredits2,
    CumulativeGPA is TotalGradePoints / TotalCredits.

% If only one semester data is available, the cumulative GPA is the same as the GPA for that semester
cumulative_gpa(Semester, GPA) :-
    (gpa(Semester, GPA) ->
        true
    ;
        default_gpa(GPA)
    ).

% % Facts
% %grade(module1, semester1, 4.30).
% %grade(module2, semester1, 3.67).
% %grade(module3, semester1, 3.00).
% %grade(module4, semester1, 3.33).
% %grade(module5, semester1, 4.00).

% %credit(module1, 1).
% %credit(module2, 4).
% %credit(module3, 3).
% %credit(module4, 4).
% %credit(module5, 2).

% % Calculate grade points earned for each module
% grade_points(Module, Semester, GradePoints) :-
%     grade(Module, Semester, Grade),
%     credit(Module, Credit),
%     GradePoints is Grade * Credit.

% % Calculate total grade points and total credits for a semester
% semester_totals(Semester, TotalGradePoints, TotalCredits) :-
%     findall(GradePoints, grade_points(_, Semester, GradePoints), GradePointsList),
%     sum_list(GradePointsList, TotalGradePoints),
%     findall(Credit, (grade(Module, Semester, _), credit(Module, Credit)), CreditsList),
%     sum_list(CreditsList, TotalCredits).

% % Calculate GPA for a semester
% gpa(Semester, GPA) :-
%     semester_totals(Semester, TotalGradePoints, TotalCredits),
%     GPA is TotalGradePoints / TotalCredits.

% % Calculate cumulative GPA for two semesters
% cumulative_gpa(Semester1, Semester2, CumulativeGPA) :-
%     semester_totals(Semester1, TotalGradePoints1, TotalCredits1),
%     semester_totals(Semester2, TotalGradePoints2, TotalCredits2),
%     TotalGradePoints is TotalGradePoints1 + TotalGradePoints2,
%     TotalCredits is TotalCredits1 + TotalCredits2,
%     CumulativeGPA is TotalGradePoints / TotalCredits.

% % If only one semester data is available, the cumulative GPA is the same as the GPA for that semester
% cumulative_gpa(Semester, GPA) :-
%     gpa(Semester, GPA).