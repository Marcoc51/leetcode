WITH dates AS (
    SELECT 
        student_id
        ,subject
        ,MIN(exam_date) AS first_date
        ,MAX(exam_date) AS latest_date
    FROM 
        Scores
    GROUP BY 
        student_id, subject
    HAVING COUNT(*) > 1
),
improves AS (
    SELECT
        s.student_id
        ,s.subject
        ,(
            SELECT 
              score 
            FROM 
              Scores
            WHERE 
              student_id = s.student_id
            AND 
              subject = s.subject
            AND 
              exam_date = d.first_date
        ) AS first_score
        ,(
            SELECT 
              score 
            FROM 
              Scores
            WHERE 
              student_id = s.student_id
            AND 
              subject = s.subject
            AND 
              exam_date = d.latest_date
        ) AS latest_score
    FROM 
      Scores AS s
    INNER JOIN 
      dates AS d
    ON 
      s.student_id = d.student_id 
    AND 
      s.subject = d.subject 
    AND 
      s.exam_date = d.first_date
)
SELECT
    student_id
    ,subject
    ,first_score
    ,latest_score
FROM 
    improves
WHERE 
    latest_score > first_score;
