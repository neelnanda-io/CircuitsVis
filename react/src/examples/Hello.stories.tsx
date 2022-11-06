import { ComponentStory, ComponentMeta } from "@storybook/react";

import Hello from "./Hello";

export default {
  component: Hello
} as ComponentMeta<typeof Hello>;

export const Bob: ComponentStory<typeof Hello> = () => <Hello name="Bob" />;
