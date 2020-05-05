import React from "react";
import { Col, Row, Container } from "react-bootstrap";

function ChifCard(props) {
  return (
    <Container className=" flex-wrap w-25">
      <Row className="text-center" width="90">
        <Col className="Big-number">{props.number}</Col>
      </Row>
      <Row>
        <Col className="customText">{props.text}</Col>
      </Row>
    </Container>
  );
}

export default ChifCard;