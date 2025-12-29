# Database Metadata Source of Truth

## Core Data Flow
- **Projects** are the top-level containers.
- **Microsurveys** belong to Projects and define the feedback form.
- **Feeds** are the actual responses (submissions) from users linked to a Microsurvey.
- **Feed Questions** are the specific answers given in a Feed.
- **Questions** define the label/text of what was asked.
- **Recognitions & Awards** track employee appreciation events.


## Schema Details

### Table: audiences
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| audience_type | INTEGER |  |  |
| level | INTEGER |  |  |
| parent_id | BIGINT |  | audiences.id |
| status | INTEGER |  |  |
| archived | BOOLEAN |  |  |
| created_by | INTEGER |  |  |
| updated_by | INTEGER |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| url | VARCHAR |  |  |
| own_type | VARCHAR |  |  |


### Table: awards
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| sticker_file_id | INTEGER |  |  |
| status | INTEGER |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |


### Table: feed_question_scales
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| feed_question_id | BIGINT |  |  |
| scale_id | BIGINT |  |  |


### Table: feeds
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| microsurvey_id | BIGINT |  |  |
| microsurvey_user_id | BIGINT |  |  |
| posted_ip | VARCHAR |  |  |
| posted_browser | VARCHAR |  |  |
| device | VARCHAR |  |  |
| feed_questions_count | INTEGER |  |  |
| net_score | DOUBLE PRECISION |  |  |
| type | VARCHAR |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| audience_id | BIGINT |  | audiences.id |
| is_typ_shown | BOOLEAN |  |  |


### Table: microsurvey_questions
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| microsurvey_id | BIGINT |  |  |
| question_id | BIGINT |  |  |
| status | INTEGER |  |  |
| position | INTEGER |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |


### Table: microsurveys
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| code | INTEGER |  |  |
| name | VARCHAR |  |  |
| description | VARCHAR |  |  |
| project_id | BIGINT |  |  |
| welcome_id | BIGINT |  |  |
| thankyou_id | BIGINT |  |  |
| questions_count | INTEGER |  |  |
| feeds_count | INTEGER |  |  |
| microsurvey_users_count | INTEGER |  |  |
| set_invited_count | BOOLEAN |  |  |
| invited_count | INTEGER |  |  |
| url | VARCHAR |  |  |
| tiny_url | VARCHAR |  |  |
| audience_selected | BOOLEAN |  |  |
| response_limit | BOOLEAN |  |  |
| net_score | INTEGER |  |  |
| activated_at | TIMESTAMP |  |  |
| status | INTEGER |  |  |
| archived | BOOLEAN |  |  |
| slug | VARCHAR |  |  |
| created_by | INTEGER |  |  |
| updated_by | INTEGER |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |


### Table: projects
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| description | VARCHAR |  |  |
| project_type_id | BIGINT |  |  |
| project_group_id | BIGINT |  |  |
| microsurveys_count | INTEGER |  |  |
| default_logo | BOOLEAN |  |  |
| status | INTEGER |  |  |
| archived | BOOLEAN |  |  |
| slug | VARCHAR |  |  |
| created_by | INTEGER |  |  |
| updated_by | INTEGER |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| visited_users_data | JSONB |  |  |


### Table: reasons
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| reason_type | VARCHAR |  |  |
| category | VARCHAR |  |  |
| source | VARCHAR |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| is_default | BOOLEAN |  |  |


### Table: questions
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| description | VARCHAR |  |  |
| question_type_id | BIGINT |  |  |
| required | BOOLEAN |  |  |
| allow_strength | BOOLEAN |  |  |
| allow_comment | BOOLEAN |  |  |
| allow_image | BOOLEAN |  |  |
| allow_branching | BOOLEAN |  |  |
| question_strength_id | BIGINT |  |  |
| question_scale_id | BIGINT |  |  |
| max_length | INTEGER |  |  |
| text_type | VARCHAR |  |  |
| lower_scale | INTEGER |  |  |
| upper_scale | INTEGER |  |  |
| lower_scale_label | VARCHAR |  |  |
| upper_scale_label | VARCHAR |  |  |
| label | VARCHAR |  |  |
| prompt_text | VARCHAR |  |  |
| dropdown | BOOLEAN |  |  |
| na_option | BOOLEAN |  |  |
| question_option_type | INTEGER |  |  |
| lookup_data_option | INTEGER |  |  |
| lookup_select_mode | INTEGER |  |  |
| hide_unwanted_words | BOOLEAN |  |  |
| shared | BOOLEAN |  |  |
| status | INTEGER |  |  |
| archived | BOOLEAN |  |  |
| type | VARCHAR |  |  |
| created_by | INTEGER |  |  |
| updated_by | INTEGER |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| rtlx_x_id | BIGINT |  | data_attributes.id |
| rtlx_options | ARRAY |  |  |
| project_type_id | INTEGER |  |  |
| comment_prompt | TEXT |  |  |


### Table: question_scales
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |


### Table: question_strengths
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |


### Table: rankings
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| audience_id | BIGINT |  |  |
| rankable_type | VARCHAR |  |  |
| rankable_id | BIGINT |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |


### Table: scales
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| name | VARCHAR |  |  |
| question_scale_id | BIGINT |  |  |
| position | INTEGER |  |  |


### Table: recognitions
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| user_id | BIGINT |  | users.id |
| feed_question_id | BIGINT |  | feed_questions.id |
| award_id | BIGINT |  | awards.id |
| comment | TEXT |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| recognized_by_id | BIGINT |  | users.id |


### Table: feed_questions
| Column | Type | PK | FK |
|--------|------|----|----|
| id | BIGINT | Yes |  |
| feed_id | BIGINT |  |  |
| microsurvey_id | BIGINT |  |  |
| question_id | BIGINT |  |  |
| jf_type | INTEGER |  |  |
| strength_id | BIGINT |  |  |
| content | VARCHAR |  |  |
| comment | TEXT |  |  |
| posted_ip | VARCHAR |  |  |
| magnitude | DOUBLE PRECISION |  |  |
| score | DOUBLE PRECISION |  |  |
| status | INTEGER |  |  |
| type | VARCHAR |  |  |
| created_at | TIMESTAMP |  |  |
| updated_at | TIMESTAMP |  |  |
| action_status | VARCHAR |  |  |
| resolved_positively | VARCHAR |  |  |
| action_comment | TEXT |  |  |
| percentage | VARCHAR |  |  |
| action_taker_id | BIGINT |  | users.id |
| closed_at | TIMESTAMP |  |  |
| expired_at | TIMESTAMP |  |  |
| reason_id | BIGINT |  | reasons.id |
| mixed_signal | BOOLEAN |  |  |
| mixed_signal_reason | TEXT |  |  |
| recognition_opportunity | BOOLEAN |  |  |
| recognition_summary | TEXT |  |  |
| analysis_processed_at | TIMESTAMP |  |  |
| analysis_error | TEXT |  |  |

