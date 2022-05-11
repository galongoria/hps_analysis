inv_df = read_csv(here("data/clean_data_322.csv"))

monthly_counts = inv_df %>%
  count(year, month)

ggplot(monthly_counts) +
  geom_bar(aes(x = month, y = n)) +
  facet_wrap(~year)
