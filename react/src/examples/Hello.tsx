import React from "react";
import PropTypes from "prop-types";

/**
 * Hello Example
 */
export default function Hello({
  name
}: {
  /** Name to say "Hello" to */
  name: string;
}) {
  return <p>Hello, {name}!</p>;
}

Hello.propTypes = {
  name: PropTypes.string.isRequired
};
