from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    ALLOWED_PLATFORMS = ['Instagram', 'YouTube', 'Twitter']
    def setUp(self) -> None:
        self.media = SocialMedia("Kehana", "Instagram", 1000, "videos")
        self.media_with_posts = SocialMedia("Doni", "Twitter", 1000, "cars")
        self.media_with_posts._posts = [{'content': "cars", 'likes': 10, 'comments': []}]

    def test_correct_init(self):
        self.assertEqual("Kehana", self.media._username)
        self.assertEqual("Instagram", self.media._platform)
        self.assertEqual(1000, self.media._followers)
        self.assertEqual("videos", self.media._content_type)
        self.assertEqual([], self.media._posts)

    def test_init_with_negative_followers_expected_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.media.followers = -1
        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test__validate_and_set_platform_with_invalid_platform_expected_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.media.platform = "Facebook"
        self.assertEqual(f"Platform should be one of {self.ALLOWED_PLATFORMS}", str(ve.exception))

    def test_create_post_expect_success(self):
        expected_msg = f"New {self.media._content_type} post created by {self.media._username} " \
                       f"on {self.media._platform}."
        result = self.media.create_post("cat video")
        self.assertEqual(expected_msg, result)
        self.assertEqual([{'comments': [], 'content': 'cat video', 'likes': 0}], self.media._posts)

    def test_like_post_with_valid_index_and_0_likes_expect_success(self):
        self.media.create_post("cat video")
        self.media.create_post("dog video")
        expected_msg = f"Post liked by {self.media._username}."
        result = self.media.like_post(0)
        self.assertEqual(expected_msg, result)
        self.assertEqual(1, self.media._posts[0]["likes"])

    def test_like_post_with_valid_index_and_10_likes_expect_success(self):
        expected_msg = f"Post has reached the maximum number of likes."
        result = self.media_with_posts.like_post(0)
        self.assertEqual(expected_msg, result)

    def test_like_post_with_invalid_index_and_10_likes_expect_success(self):
        expected_msg = "Invalid post index."
        result = self.media_with_posts.like_post(1)
        self.assertEqual(expected_msg, result)

    def test_comment_on_post_with_long_comment_expect_success(self):
        expected_msg = f"Comment added by {self.media_with_posts._username} on the post."
        result = self.media_with_posts.comment_on_post(0, "nice brooom broom car!")
        self.assertEqual(expected_msg, result)

    def test_comment_on_post_with_short_comment_expect_success(self):
        expected_msg = "Comment should be more than 10 characters."
        result = self.media_with_posts.comment_on_post(0, "nice car!")
        self.assertEqual(expected_msg, result)


if __name__ == "__main__":
    main()
